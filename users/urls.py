from django.urls import path
from django import views

from . import views

urlpatterns = [
    path('user/signup/', views.CreateUserView.as_view()),
    path('user/signin/', views.LoginView.as_view()),
    path('user/', views.ListUserView.as_view()),
    path('user/<pk>/', views.RetrieveUpdateDestroyUserView.as_view()),
]