from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "full_name",
            "birth_date",
            "phone",
            "password",
            "is_debt",
            "created_at"
        ]
        read_only = "id"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)

class UserLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
        ]

