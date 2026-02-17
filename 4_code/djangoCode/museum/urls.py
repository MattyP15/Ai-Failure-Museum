from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect


def curator_redirect(request):
    return redirect('curator_dashboard')

urlpatterns = [


    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path("privacy/", views.privacy_policy, name="privacy"),
    path("delete-my-data/", views.delete_my_data, name="delete_my_data"),
    
    ##curator stuffs
    path("curator/dashboard/", views.curator_dashboard, name="curator_dashboard"),
    path("curator/create/", views.create_exhibit, name="create_exhibit"),
    path("curator/edit/<int:exhibit_id>/", views.edit_exhibit, name="edit_exhibit"),
    path("curator/analytics/", views.analytics_view, name="analytics_dashboard"),
    path("curator/create-quiz/", views.create_quiz, name="create_quiz"),
    path("curator/delete/<int:exhibit_id>/", views.delete_exhibit, name="delete_exhibit"),
    path("curator/", curator_redirect, name="curator_redirect"),
    
    ##public routes
    path("exhibit/<int:exhibit_id>/", views.exhibit_detail, name="exhibit_detail"),
    path("quiz/<int:quiz_id>/", views.take_quiz, name="take_quiz"),
    path("quiz/<int:quiz_id>/submit/", views.submit_quiz, name="submit_quiz"),

## wquizz stuffs
    path("api/quizzes/", views.api_quizzes, name="api_quizzes"),
    path("api/quizzes/<int:quiz_id>/", views.api_quiz_detail, name="api_quiz_detail"),
    path("api/quizzes/<int:quiz_id>/submit/", views.api_quiz_submit, name="api_quiz_submit"),
]
