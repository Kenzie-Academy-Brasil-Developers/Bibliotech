from django.urls import path

from books.views import BookView, BookViewDetail

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:book_id>/', BookViewDetail.as_view())
]