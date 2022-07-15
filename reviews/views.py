from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from reviews.models import Review
from books.models import Book
from reviews.serializers import ReviewSerializer

class ListCreateBookReviewView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs['pk'])
        serializer.save(book=book, user=self.request.user)
    
    def get_queryset(self):
        reviews = Review.objects.filter(book__id=self.kwargs['pk'])
        return reviews
    

