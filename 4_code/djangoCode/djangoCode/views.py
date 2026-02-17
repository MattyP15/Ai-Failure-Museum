
from django.shortcuts import render, get_object_or_404
from museum.models import Category, Exhibit


def homepage(request):
    categories = Category.objects.all()
    return render(request, "main.html", {'categories': categories})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    exhibits = category.exhibits.all() if hasattr(category, 'exhibits') else Exhibit.objects.filter(category=category)
    return render(request, "category.html", {'category': category, 'exhibits': exhibits})

def login(request):
    return render(request, "login.html")

