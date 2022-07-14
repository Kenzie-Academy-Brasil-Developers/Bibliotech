from wsgiref.validate import validator
from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=127)
    pages = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    classification = models.PositiveIntegerField()
    #genre = models.ForeignKey('genre.Genre', on_delete=models.PROTECT)
    #review = models.ForeignKey('reviews.Review', on_delete=models.CASCADE)
