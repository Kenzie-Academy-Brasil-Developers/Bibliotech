from django.urls import path
from django import views

from . import views

urlpatterns = [
    path('user/signup/', views.ListCreateUserView.as_view()),
    path('user/signin/', views.LoginView.as_view()),
]