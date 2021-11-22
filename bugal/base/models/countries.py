"""Country Model."""

# Django
from django.db import models


class Country(models.Model):
    """Country model

    Creates Countries table.
    """

    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        """Return Country name string representation"""
        return self.name
