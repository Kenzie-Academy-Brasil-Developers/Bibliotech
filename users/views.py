from django.contrib.auth import authenticate

from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.permissions import IsOwnerOrAdmin, IsDebt


from users.models import User
from users.serializers import LoginSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
        
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)


        user = authenticate(
            username=serializer.validated_data["email"], 
            password=serializer.validated_data["password"]
        )

        if user:
           token, _ = Token.objects.get_or_create(user=user)

           return Response({"token": token.key})

        return Response(
            {"detail": "invalid email or password"}, status.HTTP_401_UNAUTHORIZED)

class RetrieveUpdateDestroyUserView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]  

    queryset = User
    serializer_class = UserSerializer