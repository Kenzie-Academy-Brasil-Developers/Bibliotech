from django.urls import path
from django import views
from . import views

urlpatterns = [
    path('loan/', views.ListCreateLoanView.as_view()),
    path('loan/all', views.ListCreateLoanView.as_view()),
    path('loan/<int:pk>/', views.ListCreateLoanView.get_queryset.as_view())
]