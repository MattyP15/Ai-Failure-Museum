import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .gamification import award_points
from .models import Quiz, Question, AnswerOption, QuizAttempt, Response, UserBadge
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

    # Delete quiz attempts & responses via cascade
    QuizAttempt.objects.filter(user=user).delete()

    # Delete user badges
    UserBadge.objects.filter(user=user).delete()

    # Finally delete the account (profile cascades)
    user.delete()

    return redirect("/")


def curator_dashboard(request):
    if not is_curator(request.user):
        return redirect("/login/?next=/curator/")

    return render(request, "curator_dashboard.html")


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
