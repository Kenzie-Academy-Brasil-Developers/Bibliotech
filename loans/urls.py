from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('loan/', views.ListLoansView.as_view()),
    path('loan/<int:pk>/', views.LoanDetailView.as_view())
]