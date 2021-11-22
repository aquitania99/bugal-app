# Django
from django.db import models

# Models
from .contacts import Contact
from .shifts import Shift
from .users import User
from .expenses import Expense


class Invoice(models.Model):
    """Invoice model.

    Invoices created by the user.
    """

    CHOICES = (
        ('SE', 'SavedExit'),
        ('SS', 'SavedSent'),
        ('U', 'Unpaid'),
        ('P', 'Paid'),
        ('WO', 'WriteOff')
    )

    ref = models.CharField(max_length=12, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    amount_cash = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=3, choices=CHOICES, default='', blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    rate_name = models.CharField('rate name', max_length=100, blank=True, null=True)
    rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.status


