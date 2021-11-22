"""Organisation Model."""

# Django
from django.db import models

# Models
from bugal.base.models.common_models import CommonPhoneAddress


class Organisation(CommonPhoneAddress):
    """Organisation model

    Creates Organisation table. Used by the Bugal's User and Client
    """
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    client = models.ManyToManyRel('id', 'Client', 'client')
    name = models.CharField(max_length=255, null=True)
    
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    def __str__(self):
        """Return User's string representation"""
        return f'{self.name}'
