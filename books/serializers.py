from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "pages", "author", "classification"]

    #def validate_classification(self):
    #    if self.classification < 1 or self.classification > 10:
     #       raise serializers.ValidationError("classification must be de 1 a 10")