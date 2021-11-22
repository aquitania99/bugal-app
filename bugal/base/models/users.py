"""User Model."""

# Python
import uuid

# Django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Utilities
from .common_models import BugalCommonUserModel, CommonPhoneAddress


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and Saves a New User"""
        if not email:
            raise ValueError('Users most have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name="", last_name=""):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.first_name = first_name
        user.last_name = last_name
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin, BugalCommonUserModel, CommonPhoneAddress):
    """User model

    Extends from Django's Abstract User and Bugal Common User,
    change the username field to email and add some extra fields.
    """

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    email = models.EmailField(
        'email address',
        max_length=255,
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when the user have verified its email address.'
    )
    
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Set to true by default when the user is created'
    )
    
    is_staff = models.BooleanField(
        'staff',
        default=False,
        help_text='Set to false by default when the user is created'
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        """Return username"""
        return str(self.uuid)
        # return f'{self.first_name} {self.last_name} uuid {self.uuid}'

    def get_short_name(self):
        """Return username"""
        return str(self.uuid)

