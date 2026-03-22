import json
from urllib import request

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .gamification import award_points
from .models import Quiz, Question, AnswerOption, QuizAttempt, Response, UserBadge, TimelineEvent
from .rbac import is_curator
from django.contrib.auth.decorators import login_required
from .models import Exhibit, Category, Comment, Bookmark, UserSubmission
from .forms import ExhibitForm, QuizForm, CommentForm, UserSubmissionForm
from .rbac import is_curator


def privacy_policy(request):
    return render(request, "privacy.html")


@login_required
def delete_my_data(request):
    if request.method == "GET":
        return render(request, "delete_my_data.html")

    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method")

    user = request.user

    # delete quiz attempts & responses via cascade
    QuizAttempt.objects.filter(user=user).delete()

    # Delete user badges
    UserBadge.objects.filter(user=user).delete()

    # Finally delete the account (profile cascades)
    user.delete()

    return redirect("/")


def curator_dashboard(request):

    active_exhibits = Exhibit.objects.filter(is_archived=False)
    user_submissions = UserSubmission.objects.filter(status='pending')
    archived_exhibits = Exhibit.objects.filter(is_archived=True)
    categories = Category.objects.all()
    total_quizzes = Quiz.objects.count()
    bookmarked_exhibits = Exhibit.objects.none()
    if request.user.is_authenticated:
        bookmarked_exhibits = Exhibit.objects.filter(
            bookmarks__user=request.user
        ).select_related('category').distinct()
    ##add more stats for curator dashboard :) 

    return render(request, 'curator/dashboard.html', {
        'categories': categories,
        'active_exhibits': active_exhibits,
        'archived_exhibits': archived_exhibits,
        'total_quizzes': total_quizzes,
        'bookmarked_exhibits': bookmarked_exhibits,
        'user_submissions' : user_submissions})




def api_quizzes(request):
    quizzes = Quiz.objects.filter(is_active=True).order_by("id")
    data = [{"id": q.id, "title": q.title, "description": q.description} for q in quizzes]
    return JsonResponse({"quizzes": data})


def api_quiz_detail(request, quiz_id: int):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    questions = []
    for q in quiz.questions.all():
        questions.append(
            {
                "id": q.id,
                "prompt": q.prompt,
                "qtype": q.qtype,
                "options": [{"id": o.id, "text": o.text} for o in q.options.all()],
            }
        )
    return JsonResponse(
        {
            "id": quiz.id,
            "title": quiz.title,
            "description": quiz.description,
            "points_for_completion": quiz.points_for_completion,
            "questions": questions,
        }
    )


@csrf_exempt  # OK for prototype; remove once your frontend sends CSRF token
@login_required
def api_quiz_submit(request, quiz_id: int):
    if request.method != "POST":
        return HttpResponseBadRequest("POST required")

    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")

    answers = payload.get("answers", [])
    if not isinstance(answers, list):
        return HttpResponseBadRequest("answers must be a list")

    attempt = QuizAttempt.objects.create(user=request.user, quiz=quiz)

    for a in answers:
        qid = a.get("question_id")
        if not qid:
            continue

        question = get_object_or_404(Question, id=qid, quiz=quiz)

        selected_option = None
        text_answer = ""

        if question.qtype == Question.MULTIPLE_CHOICE:
            oid = a.get("option_id")
            if oid:
                selected_option = get_object_or_404(AnswerOption, id=oid, question=question)
        else:
            text_answer = (a.get("text") or "").strip()

        Response.objects.create(
            attempt=attempt,
            question=question,
            selected_option=selected_option,
            text_answer=text_answer,
        )

    total_points, newly_awarded = award_points(request.user, quiz.points_for_completion)

    return JsonResponse(
        {
            "status": "ok",
            "attempt_id": attempt.id,
            "points_awarded": quiz.points_for_completion,
            "total_points": total_points,
            "new_badges": [{"code": b.code, "name": b.name} for b in newly_awarded],
        }
    )

@login_required

def create_exhibit(request):
    if not is_curator(request.user):
        messages.error(request, "You do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard ')
    if request.method == 'POST' : 
        form = ExhibitForm(request.POST, request.FILES)
        if form.is_valid():
            exhibit = form.save()
            messages.success(request, f'Exhibit "{exhibit.title}" created successfully')
            return redirect('curator_dashboard')
    else:
        form = ExhibitForm()

    return render(request, 'curator/create_exhibit.html', {'form': form})

##functions for delete, archieve, edit

@login_required
def analytics_view(request):
    if not is_curator(request.user):
        messages.error(request, "you do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard ')
    return render(request, 'curator/analytics.html')

@login_required
def create_quiz(request):
    if not is_curator(request.user):
        messages.error(request, "You do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard')
    
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            messages.success(request, f'Quiz "{quiz.title}" created successfully')
            return redirect('curator_dashboard')
    else:
        form = QuizForm()
    
    return render(request, 'curator/create_quiz.html', {'form': form})

def exhibit_detail(request, exhibit_id):
    try:
        categories = Category.objects.all()
        exhibit = get_object_or_404(Exhibit, id=exhibit_id)
        if exhibit.is_archived and not is_curator(request.user):
            messages.error(request, "This exhibit is archived and not available to the public.")
            return redirect('/')

        if request.method == 'POST' and request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.exhibit = exhibit
                new_comment.user = request.user
                new_comment.save()
                return redirect('exhibit_detail', exhibit_id=exhibit_id)
        else:
            comment_form = CommentForm()

        quizzes = exhibit.quizzes.filter(is_active=True)
        timeline_events = exhibit.timeline_events.all()
        comments = exhibit.comments.all()

        is_bookmarked = False
        if request.user.is_authenticated:
            is_bookmarked = Bookmark.objects.filter(user=request.user, exhibit=exhibit).exists()

        return render(request, 'curator/exhibit_detail.html', {
            'exhibit': exhibit,
            'quizzes': quizzes,
            'categories': categories,
            'timeline_events': timeline_events,
            'comments': comments,
            'comment_form': comment_form,
            'is_bookmarked': is_bookmarked,
        })
    except Exception as e:
        messages.error(request, f'Error loading exhibit: {str(e)}')
        return redirect('/')

def take_quiz(request, quiz_id):
    try:
        quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
        questions = quiz.questions.all()
        return render(request, 'quiz/take_quiz.html', {'quiz': quiz, 'questions': questions})
    except Exception as e:
        messages.error(request, f'Error loading quiz: {str(e)}')
        return redirect('/')


def submit_quiz(request, quiz_id):
    try:
        quiz = get_object_or_404(Quiz, id=quiz_id)

        if request.method == 'POST':
            responses_data = []
            correct_count = 0
            total_count = 0

            # Only create an attempt record if the user is logged in
            attempt = None
            if request.user.is_authenticated:
                attempt = QuizAttempt.objects.create(user=request.user, quiz=quiz)

            for question in quiz.questions.all():
                if question.qtype == 'mc':
                    # Multiple choice - get selected option ID
                    option_id = request.POST.get(f'question_{question.id}')
                    if option_id:
                        try:
                            selected_option = AnswerOption.objects.get(id=option_id, question=question)

                            if attempt:
                                Response.objects.create(
                                    attempt=attempt,
                                    question=question,
                                    selected_option=selected_option
                                )

                            is_correct = selected_option.is_correct
                            if is_correct:
                                correct_count += 1
                            total_count += 1

                            responses_data.append({
                                'question': question.prompt,
                                'answer': selected_option.text,
                                'is_correct': is_correct,
                                'correct_answer': question.options.filter(is_correct=True).first().text if not is_correct else None
                            })
                        except AnswerOption.DoesNotExist:
                            pass
                else:
                    # Text answer
                    answer = request.POST.get(f'question_{question.id}', '').strip()
                    if answer:
                        if attempt:
                            Response.objects.create(
                                attempt=attempt,
                                question=question,
                                text_answer=answer
                            )
                        responses_data.append({
                            'question': question.prompt,
                            'answer': answer,
                            'is_correct': None  # No grading for text answers
                        })

            # Award points only if logged in
            points_earned = correct_count
            if request.user.is_authenticated:
                award_points(request.user, points_earned)

            return render(request, 'quiz/quiz_results.html', {
                'quiz': quiz,
                'responses': responses_data,
                'points': points_earned if request.user.is_authenticated else None,
                'exhibit': quiz.exhibit,
                'correct_count': correct_count,
                'total_count': total_count
            })

        return redirect('take_quiz', quiz_id=quiz_id)
    except Exception as e:
        messages.error(request, f'Error submitting quiz: {str(e)}')
        return redirect('/')


@login_required
def edit_exhibit(request, exhibit_id):
    if not is_curator(request.user):
        messages.error(request, "You do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard')

    try:
        exhibit = get_object_or_404(Exhibit, id=exhibit_id)
        quiz = exhibit.quizzes.first() if exhibit.quizzes.exists() else None

        if request.method == 'POST':
            exhibit_form = ExhibitForm(request.POST, request.FILES, instance=exhibit)

            if exhibit_form.is_valid():
                exhibit = exhibit_form.save()

                quiz_title = request.POST.get('quiz_title', '').strip()
                if quiz_title:
                    if quiz:
                        quiz.title = quiz_title
                        quiz.description = request.POST.get('quiz_description', '')
                        quiz.save()
                    else:
                        quiz = Quiz.objects.create(
                            exhibit=exhibit,
                            title=quiz_title,
                            description=request.POST.get('quiz_description', ''),
                            is_active=True,
                            points_for_completion=10
                        )

                    quiz.questions.all().delete()
                    question_count = int(request.POST.get('question_count', 0))
                    for i in range(1, question_count + 1):
                        prompt = request.POST.get(f'question_{i}_prompt', '').strip()
                        if not prompt:
                            continue
                        question = Question.objects.create(
                            quiz=quiz, prompt=prompt,
                            qtype=Question.MULTIPLE_CHOICE, order=i,
                        )
                        option_count = int(request.POST.get(f'question_{i}_option_count', 0))
                        correct = request.POST.get(f'question_{i}_correct')
                        for j in range(1, option_count + 1):
                            text = request.POST.get(f'question_{i}_option_{j}', '').strip()
                            if not text:
                                continue
                            AnswerOption.objects.create(
                                question=question, text=text,
                                is_correct=(str(j) == correct), order=j,
                            )

                exhibit.timeline_events.all().delete()
                event_count = int(request.POST.get('event_count', 0))
                for i in range(1, event_count + 1):
                    year = request.POST.get(f'event_{i}_year', '').strip()
                    description = request.POST.get(f'event_{i}_description', '').strip()
                    if year and description:
                        TimelineEvent.objects.create(
                            exhibit=exhibit,
                            year=year,
                            description=description,
                            order=i,
                        )

                messages.success(request, f'Exhibit "{exhibit.title}" updated successfully')
                return redirect('curator_dashboard')
        else:
            exhibit_form = ExhibitForm(instance=exhibit)

        questions = quiz.questions.all() if quiz else []
        timeline_events = exhibit.timeline_events.all()

        return render(request, 'curator/edit_exhibit.html', {
            'form': exhibit_form,
            'exhibit': exhibit,
            'quiz': quiz,
            'questions': questions,
            'timeline_events': timeline_events,
        })
    except Exception as e:
        messages.error(request, f'Error: {str(e)}')
        return redirect('curator_dashboard')

@login_required
def delete_exhibit(request, exhibit_id):
    if not is_curator(request.user):
        messages.error(request, "you do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard ')
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)

    if request.method == 'POST':
        exhibit_title = exhibit.title
        exhibit.delete()
        messages.success(request, f'exhibit "{exhibit_title}" deleted successfully')
        return redirect('curator_dashboard')

    return render(request, 'curator/dashboard.html', {'active_exhibits': Exhibit.objects.filter(is_active=True)})

@login_required
def toggle_archive_exhibit(request, exhibit_id):
    if not is_curator(request.user):
        print(request, "you do not have curator permissions")
        return redirect('/login/?next=/curator/dashboard ')
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)

    
    exhibit_title = exhibit.title
    exhibit.is_archived = not exhibit.is_archived
    exhibit.save()

    action = "archived" if exhibit.is_archived else "unarchived"
    print(request, f'exhibit "{exhibit_title}" {action} successfully')
    return redirect('curator_dashboard')


@login_required
def toggle_bookmark(request, exhibit_id):
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, exhibit=exhibit)
    if not created:
        bookmark.delete()
    return redirect('exhibit_detail', exhibit_id=exhibit_id)


@login_required
def my_bookmarks(request):
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('exhibit', 'exhibit__category')
    return render(request, 'museum/my_bookmarks.html', {
        'bookmarks': bookmarks,
    })


def community_gallery(request):
    submissions = UserSubmission.objects.filter(status=UserSubmission.APPROVED).select_related('author', 'category')
    return render(request, 'community/gallery.html', {
        'submissions': submissions,
    })


def community_submission_detail(request, submission_id):
    submission = get_object_or_404(UserSubmission, id=submission_id, status=UserSubmission.APPROVED)
    return render(request, 'community/submission_detail.html', {
        'submission': submission,
    })


@login_required
def submit_exhibit(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.author = request.user
            submission.save()
            messages.success(request, 'Your exhibit has been submitted for review.')
            return redirect('community_gallery')
    else:
        form = UserSubmissionForm()
    return render(request, 'community/submit.html', {
        'form': form,
    })


@login_required
def my_submissions(request):
    submissions = UserSubmission.objects.filter(author=request.user)
    return render(request, 'community/my_submissions.html', {
        'submissions': submissions,
    })


@login_required
def review_pool(request):
    if not is_curator(request.user):
        messages.error(request, "You do not have curator permissions")
        return redirect('/')
    pending = UserSubmission.objects.filter(status=UserSubmission.PENDING).select_related('author', 'category')
    return render(request, 'curator/review_pool.html', {
        'pending': pending,
    })


@login_required
def review_submission(request, submission_id):
    if not is_curator(request.user):
        messages.error(request, "You do not have curator permissions")
        return redirect('/')
    submission = get_object_or_404(UserSubmission, id=submission_id)
    if request.method == 'POST':
        from django.utils import timezone
        action = request.POST.get('action')
        note = request.POST.get('reviewer_note', '')
        submission.reviewed_by = request.user
        submission.reviewer_note = note
        submission.reviewed_at = timezone.now()
        if action == 'approve':
            submission.status = UserSubmission.APPROVED
            messages.success(request, f'"{submission.title}" has been approved.')
        elif action == 'deny':
            submission.status = UserSubmission.DENIED
            messages.success(request, f'"{submission.title}" has been denied.')
        submission.save()
        return redirect('review_pool')
    return render(request, 'curator/review_submission.html', {
        'submission': submission,
    })
  
