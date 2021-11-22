# Django
from django.db import models


class ShiftType(models.Model):
    """Shift Types model.

    List of Shift types, used by users and clients.
    """

    name = models.CharField('shift type', max_length=100)

    def __str__(self):
        return self.name
