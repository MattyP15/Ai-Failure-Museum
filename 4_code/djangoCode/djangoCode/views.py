from django.shortcuts import render

def homepage(request):
    return render(request, "main.html")

def category(request):
    return render(request, "category.html")

def login(request):
    return render(request, "login.html")

