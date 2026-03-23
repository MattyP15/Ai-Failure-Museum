"""
URL configuration for djangoCode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from .forms import UserLoginForm

urlpatterns = [

    path("admin/", admin.site.urls),
    path("", views.homepage),
    path("category/<slug:slug>/", views.category, name="category_detail"),
    path("submit/", views.submit_page, name="submit_page"),
    path("login/", auth_views.LoginView.as_view(template_name='registration/login.html', authentication_form=UserLoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', include('museum.urls')),
    path('search/', views.search, name="search"),
    path('about/', views.about, name="about"),
    path('termsOfService/', views.terms_of_service, name="terms_of_service"),
    path('accessibility/', views.accessibility, name="accessibility"),
    path('explore/', views.explore, name="explore"),
    path('exhibits/', views.exhibits_browse, name="exhibits_browse"),
    path('profile/', views.profile, name="profile"),
]
