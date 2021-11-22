"""BankAccount Model."""

# Django
from django.db import models


class BankAccount(models.Model):
    """BankAccount model

    Creates BankAccount table. Used by the User
    """

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)

    bsb = models.PositiveIntegerField(default=0)
    number = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return User's string representation"""
        return self.bank.name
