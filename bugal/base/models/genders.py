"""Gender Model."""

# Django
from django.db import models


class Gender(models.Model):
    """Gender model

    Creates Gender table. Used on User and Client
    """
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
        ('N/A', 'N/A')
    )

    identity = models.CharField(max_length=20, choices=CHOICES, unique=True, default='N/A')
    description = models.CharField(max_length=20, blank=True, null=True, default='N/A')
    
    def __str__(self):
        """Return Identity string representation"""
        return self.identity
