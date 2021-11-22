# Django
from django.db import models
from bugal.base.models import User


class RateModel(models.Model):
    """Rates model.

    List of Shift types, used by users and clients.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('rate name', max_length=100)
    hourly = models.DecimalField(max_digits=6, decimal_places=2)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
