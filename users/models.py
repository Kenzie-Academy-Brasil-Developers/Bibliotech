from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import CustomUserManager

class User(AbstractUser):    

    email = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=70)
    birth_date = models.DateField()
    phone = models.CharField(max_length=12)
    is_debt = models.BooleanField(default=False, null=True)
    created_at = models.DateField(auto_now_add=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "birth_date", "phone", "is_debt"]
    objects = CustomUserManager()