"""Expense Categories Model."""

# Django
from django.db import models


class ExpenseCategory(models.Model):
    """Expense Category model."""

    name = models.CharField('expense name', max_length=100)
    description = models.CharField('expense description', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
