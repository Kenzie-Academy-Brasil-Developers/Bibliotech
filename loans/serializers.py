from rest_framework import serializers

from loans.models import Loan
from users.serializers import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Loan
        fields = "__all__"
        
    def create(self, validated_data):
        loan = Loan.objects.create(**validated_data)

        return loan