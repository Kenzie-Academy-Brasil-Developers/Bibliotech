from django.urls import path
from . import views

urlpatterns = [
    path('book/<pk>/review/', views.ListCreateReviewView.as_view()),
    path('review/<pk>/', views.RetrieveUpdateDestroyReviewView.as_view()),
    path('review/', views.ListReviewView.as_view())
]