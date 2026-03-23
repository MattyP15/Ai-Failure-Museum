
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from museum.models import Category, Exhibit, UserProfile, UserSubmission, UserBadge
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
    exhibits = Exhibit.objects.filter(category=category, is_archived=False).order_by('title')
    top_three = Exhibit.objects.filter(category=category, is_archived=False).order_by('-view_count')[:3]
    return render(request, "category.html", {
        'categories': categories,
        'category': category,
        'exhibits': exhibits,
        'top_three': top_three,
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
    initial_query = (request.GET.get("q") or "").strip()
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
        "initial_query": initial_query,
    })


def about(request):
    return render(request, "about.html")


def terms_of_service(request):
    return render(request, "terms_of_service.html")


def accessibility(request):
    return render(request, "accessibility.html")


def explore(request):
    category_count = Category.objects.count()
    exhibit_count = Exhibit.objects.filter(is_archived=False).count()
    submission_count = UserSubmission.objects.filter(status=UserSubmission.APPROVED).count()
    return render(request, "explore.html", {
        "category_count": category_count,
        "exhibit_count": exhibit_count,
        "submission_count": submission_count,
    })


def exhibits_browse(request):
    categories = Category.objects.annotate(exhibit_count=Count('exhibits')).order_by('name')
    all_exhibits = Exhibit.objects.filter(is_archived=False).select_related('category').order_by('-view_count')
    return render(request, "exhibits_browse.html", {
        "categories": categories,
        "all_exhibits": all_exhibits,
        "exhibit_count": all_exhibits.count(),
    })


def profile(request):
    user_points = 0
    badges = []
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_points = user_profile.points
        badges = UserBadge.objects.filter(user=request.user).select_related('badge').order_by('-awarded_at')
    return render(request, "profile.html", {
        "user_points": user_points,
        "badges": badges,
    })


def submit_page(request):
    categories = Category.objects.all()
    user_points = 0

    if not request.user.is_authenticated:
        return render(request, "submit_login.html")

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

