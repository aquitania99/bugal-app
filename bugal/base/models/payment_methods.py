# Django
from django.db import models


class PaymentMethod(models.Model):
    """Payment methods model."""

    name = models.CharField('payment method name', max_length=100)
    description = models.CharField('payment method description', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
