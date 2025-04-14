from django.db import models

# Create your models here.

class Transactions(models.Model):
    TRANSACTION_CHOICES = (
        ("CREDIT", "CREDIT"),
        ("DEBIT", "DEBIT"),
    )

    title = models.CharField(max_length=100)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.transaction_type} - {self.amount}"
