
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
    categories = Category.objects.all()
    exhibits = Exhibit.objects.filter(category=category, is_archieved=False)
    top_three = Exhibit.top_viewed(3)
    everything_else = Exhibit.the_rest(3)
    return render(request, "category.html", {
        'categories': categories,
        'category': category,
        'exhibits': exhibits,
        'top_three': top_three,
        'everything_else': everything_else,
    })



def login(request):
    return render(request, "login.html")


def search(request):
    return render(request, "search.html")