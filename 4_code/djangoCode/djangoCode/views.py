
from django.shortcuts import render, get_object_or_404
from museum.models import Category, Exhibit, UserProfile


def homepage(request):
    categories = Category.objects.all()
    user_points = 0

    # Get user points if logged in
    if request.user.is_authenticated:
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_points = user_profile.points

    return render(request, "main.html", {
        'categories': categories,
        'user_points': user_points
    })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    exhibits = category.exhibits.all() if hasattr(category, 'exhibits') else Exhibit.objects.filter(category=category)
    return render(request, "category.html", {'category': category, 'exhibits': exhibits})

def login(request):
    return render(request, "login.html")

