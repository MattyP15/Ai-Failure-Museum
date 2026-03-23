
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from museum.models import Category, Exhibit, UserProfile, UserSubmission
from .forms import UserLoginForm


def homepage(request):
    categories = Category.objects.all()
    user_points = 0

    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_points = user_profile.points

    random_exhibit = Exhibit.objects.filter(is_archived=False).order_by('?').first()

    return render(request, "main.html", {
        'categories': categories,
        'user_points': user_points,
        'random_exhibit': random_exhibit,
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    top_three = Exhibit.objects.filter(category=category, is_archived=False).order_by('-view_count')[:3]
    top_ids = top_three.values_list('id', flat=True)
    everything_else = Exhibit.objects.filter(category=category, is_archived=False).exclude(id__in=top_ids).order_by('title')
    return render(request, "category.html", {
        'categories': categories,
        'category': category,
        'exhibits': Exhibit.objects.filter(category=category, is_archived=False),
        'top_three': top_three,
        'everything_else': everything_else,
    })



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def search(request):
    user_points = 0
    categories = Category.objects.order_by("name")
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_points = user_profile.points

    approved_submissions = (
        UserSubmission.objects
        .filter(status=UserSubmission.APPROVED)
        .select_related("author", "category")
        .order_by("-submitted_at")
    )

    return render(request, "search.html", {
        "user_points": user_points,
        "categories": categories,
        "approved_submissions": approved_submissions,
    })


def about(request):
    return render(request, "about.html")


def submit_page(request):
    categories = Category.objects.all()
    user_points = 0

    if not request.user.is_authenticated:
        messages.error(request, "Please log in to submit a failure.")
        return redirect(f"/login/?next=/submit/")

    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_points = user_profile.points

    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        description = (request.POST.get("description") or "").strip()
        what_went_wrong = (request.POST.get("what_went_wrong") or "").strip()
        who_affected = (request.POST.get("who_affected") or "").strip()
        source_url = (request.POST.get("source_url") or "").strip()

        category = None
        category_id = request.POST.get("category")
        if category_id:
            category = Category.objects.filter(id=category_id).first()

        # Accept the model field name first, then fallback to any artefactN input.
        artefact = (
            request.FILES.get("artefact")
            or request.FILES.get("artefact1")
            or request.FILES.get("artefact2")
            or request.FILES.get("artefact3")
            or request.FILES.get("artefact4")
            or request.FILES.get("artefact5")
        )

        if not title or not description:
            messages.error(request, "Please fill in title and description.")
        else:
            UserSubmission.objects.create(
                author=request.user,
                title=title,
                category=category,
                description=description,
                what_went_wrong=what_went_wrong or description,
                who_affected=who_affected,
                source_url=source_url,
                artefact=artefact,
            )
            messages.success(request, "Your submission was sent for curator review.")
            return redirect("submit_page")

    return render(request, "submit.html", {
        "categories": categories,
        "user_points": user_points,
    })

