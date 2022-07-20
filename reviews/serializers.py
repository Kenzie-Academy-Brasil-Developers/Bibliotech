from rest_framework import serializers
from reviews.models import Review

from users.serializers import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['stars', 'review', 'recommendation', 'type_review', 'user']
