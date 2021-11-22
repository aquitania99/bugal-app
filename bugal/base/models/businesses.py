# Django
from django.db import models

# Models
from .users import User

class BusinessInfo(models.Model):
    """Business Info model.

    Business Info, used by users.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    abn = models.BigIntegerField(unique=True, null=True)
    gst = models.PositiveIntegerField(blank=True, null=True)
    terms = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.abn)
