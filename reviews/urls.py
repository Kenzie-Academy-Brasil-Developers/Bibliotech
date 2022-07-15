from django.urls import path
from . import views

urlpatterns = [
    path('book/<pk>/review/', views.ListCreateReviewView.as_view())
]