"""State Model."""

# Django
from django.db import models


class State(models.Model):
    """State model

    Creates Australian States table.
    """
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    name = models.CharField(max_length=30, unique=True)
    short_name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        """Return State short name string representation"""
        return self.short_name
