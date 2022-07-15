from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('loan/', views.ListLoans.as_view())
]