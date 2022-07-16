from django.db import models
from datetime import datetime, timedelta

class Loan(models.Model):
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(loan_date + timedelta(days=30))
    is_returned = models.BooleanField(default=False) 
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    ) 