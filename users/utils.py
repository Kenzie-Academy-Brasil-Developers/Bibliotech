from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, **extra_fields):        

        if not email: 
            raise ValueError("Insira um email")

        email = self.normalize_email(email)

        user = self.model(
            email=email, 
            is_superuser=is_superuser,             
            **extra_fields)

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email=email, 
            password=password,
            is_superuser=True, 
            **extra_fields
            )

    def create_user(self, email, password, **extra_fields):
            return self._create_user(
                email=email, 
                password=password, 
                is_superuser=False, 
                **extra_fields
                )

class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):

        return self.serializer_map.get(self.request.method, self.serializer_class)