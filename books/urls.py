from django.urls import path

from books.views import BookView, BookViewDetail

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<pk>/', BookViewDetail.as_view())
]
