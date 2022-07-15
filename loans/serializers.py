from rest_framework import serializers

from loans.models import Loan
from users.serializers import UserSerializer

class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = "__all__"