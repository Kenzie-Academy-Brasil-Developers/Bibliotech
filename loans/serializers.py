from rest_framework import serializers
from books.models import Book
from books.serializers import BookSerializer

from loans.models import Loan
from users.serializers import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer(many=True)
    class Meta:
        model = Loan
        fields = ["id", "loan_date", "return_date", "is_returned", "user", "book"]
        
    def create(self, validated_data):
        books_list = validated_data.pop("book")
        user = validated_data.pop("user")
        loan = Loan.objects.create(**validated_data)
        
        for item in books_list:
            book = Book.objects.get_or_create(**item)
            loan.book.add(book[0])
            loan.book.add(user)              

        return loan    
