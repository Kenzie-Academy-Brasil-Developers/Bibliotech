from wsgiref.validate import validator
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=127)
    pages = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    classification = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    genre = models.ManyToManyField('genres.Genre', related_name='book')
   