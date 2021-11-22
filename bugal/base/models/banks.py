# Django
from django.db import models


class Bank(models.Model):
    """Bank model.

    List of Banks and Financial entities, used by users and clients.
    """

    name = models.CharField('bank short name', max_length=100)
    description = models.CharField('bank name', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
