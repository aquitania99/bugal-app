"""Expenses Model."""

# Django
from django.db import models
from bugal.base.models.payment_methods import PaymentMethod
from bugal.base.models.shifts import Shift
from bugal.base.models.users import User
from bugal.base.models.contacts import Contact
from bugal.base.models.expenses_categories import ExpenseCategory


class Expense(models.Model):
    """Expense model

    Creates expenses table. Add User expenses to Shifts and Invoices.
    """

    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=False)
    amount = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)

    attachment_url = models.URLField(blank=True, null=True)

    def __str__(self):
        """Return User's string representation"""
        return self.category
