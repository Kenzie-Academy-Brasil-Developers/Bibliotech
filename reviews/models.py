from django.db import models

class TypeReview(models.TextChoices):
    CRITIQUE = "Critique"
    SUMMARY = "Summary"
    RECOMMENDATION = "Recommendation"

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    recommendation = models.CharField(max_length=50)
    type_review = models.CharField(choices=TypeReview.choices, default=TypeReview.SUMMARY, max_length=32)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    #movie