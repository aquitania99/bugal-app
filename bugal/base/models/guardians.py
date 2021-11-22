"""Guardian Model."""

# Django
from django.db import models

# Models
from .common_models import CommonPhoneAddress


class Guardian(CommonPhoneAddress):
    """Guardian model

    Creates Guardian table. Used by the Client
    """
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)

    email = models.EmailField()

    def __str__(self):
        """Return User's string representation"""
        return f'self.email'
