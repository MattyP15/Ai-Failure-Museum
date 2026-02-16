from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [



    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("privacy/", views.privacy_policy, name="privacy"),
    path("delete-my-data/", views.delete_my_data, name="delete_my_data"),
    path("curator/", views.curator_dashboard, name="curator_dashboard"),
    path("curator/create/", views.create_exhibit, name="create_exhibit"),
    path("curator/analytics/", views.analytics_view, name="analytics_dashboard"),


    path("api/quizzes/", views.api_quizzes, name="api_quizzes"),
    path("api/quizzes/<int:quiz_id>/", views.api_quiz_detail, name="api_quiz_detail"),
    path("api/quizzes/<int:quiz_id>/submit/", views.api_quiz_submit, name="api_quiz_submit"),
]
