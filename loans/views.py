from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from bibliotech.permissions import IsOwnerOrAdmin

from loans.models import Loan
from loans.serializers import LoanSerializer
    
class ListCreateLoanView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer  
            
   # def perform_create(self, serializer):
     #   loan = get_object_or_404(Loan, id=self.kwargs['pk'])
     #   print("kwargs:", self.kwargs)
      #  serializer.save(loan=loan, user=self.request.user)
    
   # def get_queryset(self):
     #   loans = Loan.objects.filter(user_id=self.kwargs['pk'])
     #   return loans
    
"""class RetrieveUpdateDestroyLoanView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer     
    """
