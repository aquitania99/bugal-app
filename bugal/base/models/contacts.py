"""Client Model."""
# Python
import uuid

# Django
from django.db import models

# Models
from .common_models import BugalCommonUserModel, CommonPhoneAddress
from .users import User
from .genders import Gender
from .guardians import Guardian

class Contact(BugalCommonUserModel, CommonPhoneAddress):
    """Contact model

    Extends from Bugal's Common User,
    Creates Contact table
    """
    CHOICES = (
        ('client', 'client'),
        ('organisation', 'organisation'),
        ('guardian', 'guardian')
    )

    RELATIONSHIPS = (
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Other family member', 'Other family member'),
        ('Friend', 'Friend'),
        ('Legal Guardian', 'Legal Guardian'),
        ('Other', 'Other')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    type = models.CharField(max_length=20, choices=CHOICES)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    org_name = models.CharField(max_length=255, null=True)
    address_line = models.CharField(max_length=255, null=True)

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A record with that email already exists.'
        }
    )
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    has_guardian = models.BooleanField(default=False)
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True)
    relationship = models.CharField(max_length=20, choices=RELATIONSHIPS, null=True, blank=True)
    soft_deleted = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        """Return client"""
        # if self.org_name:
        #     return f'{self.org_name}'
        # else:
        #     return f'{self.first_name} {self.last_name}'
        return f'{self.uuid}'
