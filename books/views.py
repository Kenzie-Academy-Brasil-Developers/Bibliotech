from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from books.permissions import IsAdminOrReadyOnly

from books.serializers import BookSerializer
from .models import Book

# Create your views here.
class BookView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminOrReadyOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookViewDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdminOrReadyOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


