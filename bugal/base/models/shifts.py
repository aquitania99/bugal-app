"""Shifts Model."""

# Django
from django.db import models


class Shift(models.Model):
    """Shifts model

    Creates Shifts table. Used by the User
    """
    STATUS = (
        ('Completed', 'Completed'),
        ('Finalised', 'Finalised'),
        ('Pending', 'Pending')
    )

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    client = models.ForeignKey('Contact', on_delete=models.CASCADE)
    shift = models.ForeignKey('ShiftType', on_delete=models.CASCADE)
    shift_name = models.CharField(max_length=50, blank=True, null=True)
    shift_comment = models.CharField(max_length=255, blank=True, null=True)
    hourly_rate = models.IntegerField(blank=True, null=True)
    meet_date = models.DateField(auto_now=False, blank=True, null=True)
    meet_time = models.TimeField(auto_now=False, blank=True, null=True)
    meet_duration = models.PositiveSmallIntegerField(blank=True, null=True)
    meet_latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    meet_longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    notification_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    repeat_shift = models.PositiveSmallIntegerField(blank=True, null=True)
    current_shift = models.PositiveSmallIntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Pending')
    
    def __str__(self):
        """Return User's string representation"""
        return self.shift_name
