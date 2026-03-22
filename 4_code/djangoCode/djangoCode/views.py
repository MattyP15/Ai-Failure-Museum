
from django.shortcuts import render, get_object_or_404
from museum.models import Category, Exhibit, UserProfile


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
    return render(request, "login.html")


def search(request):
    return render(request, "search.html")


def about(request):
    return render(request, "about.html")