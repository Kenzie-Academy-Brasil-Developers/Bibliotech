from django.shortcuts import render
from rest_framework import generics

from books.serializers import BookSerializer
from .models import Book
import ipdb

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


