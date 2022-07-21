from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from loans.mixins import SerializerByMethodMixin
from loans.permissions import IsOwnerOrAdmin, IsDebt, IsAdmin
from rest_framework.response import Response

from loans.models import Loan
from loans.serializers import ListLoanSerializer, CreateLoanSerializer
    
class ListCreateLoanView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsDebt]

    queryset = Loan.objects.all()          
    serializer_map = {
        'GET': ListLoanSerializer,
        'POST': CreateLoanSerializer,
    }          

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, book_id=self.request.data["book_id"])

class RetrieveLoanView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Loan
    serializer_class = ListLoanSerializer

    
class DestroyLoanView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
    queryset = Loan
    serializer_class = ListLoanSerializer     
