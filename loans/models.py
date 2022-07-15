from django.db import models

class Loan(models.Model):
    loan_date = models.DateField()
    return_date = models.DateField()
    is_returned = models.BooleanField()  # qual é o valor default?
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    )    
