from rest_framework import serializers
from books.models import Book
from books.serializers import BookSerializer

from loans.models import Loan
from users.serializers import UserSerializer, UserLoanSerializer

class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"

        
class CreateLoanSerializer(serializers.ModelSerializer):

    user = UserLoanSerializer(read_only=True)
    
    class Meta:
        model = Loan
        fields = "__all__"
        read_only_fields = ["id", "loan_date", "return_date", "is_returned", "user", "book_id"]

    def create(self, validated_data):
        book_data = validated_data.pop("book_id")
        book = Book.objects.get(id=book_data)
        loan = Loan.objects.create(**validated_data, book_id=book)      
        return loan    


class ListLoanSerializer(serializers.ModelSerializer):
    user = UserLoanSerializer(read_only=True)

    class Meta:
        model = Loan
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        book_data = validated_data.pop("book_id")
        book = Book.objects.get(id=book_data)
        loan = Loan.objects.create(**validated_data, book_id=book)      
        return loan  
