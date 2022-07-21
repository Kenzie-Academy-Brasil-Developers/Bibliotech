from asyncore import read
from rest_framework import serializers
from reviews.models import Review

from users.serializers import UserSerializer
from books.serializers import BookSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)


    class Meta:
        model = Review
        fields = ['id', 'stars', 'review', 'recommendation', 'type_review', 'user', "book"]
        read_only_fields = ["book"]
        depth = 2
