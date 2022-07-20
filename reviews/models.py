from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class TypeReview(models.TextChoices):
    CRITIQUE = "Critique"
    SUMMARY = "Summary"
    RECOMMENDATION = "Recommendation"

class Review(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    review = models.TextField()
    recommendation = models.CharField(max_length=50)
    type_review = models.CharField(choices=TypeReview.choices, default=TypeReview.SUMMARY, max_length=32)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="reviews")