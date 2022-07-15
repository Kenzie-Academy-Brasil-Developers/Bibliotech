from django.db import models

class Loan(models.Model):
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False) 
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    )    
