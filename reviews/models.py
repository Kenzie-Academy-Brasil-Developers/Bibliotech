from django.db import models

class TypeReview(models.TextChoices):
    CHOICE_1 = "c1"
    CHOICE_2 = "c2"
    CHOICE_3 = "c3"
    CHOICE_4 = "c4"

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    recommendation = models.CharField(max_length=50)
    type_review = models.CharField(choices=TypeReview.choices, default=TypeReview.CHOICE_1, max_length=32)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    #movie