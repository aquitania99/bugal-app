"""Invoice Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import Invoice

# Serializers
from bugal.users.serializers import ExpenseSerializer


class InvoiceModelSerializer(serializers.ModelSerializer):
    """Invoice basic information serializer"""
    expenses = ExpenseSerializer(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = Invoice

        fields = (
            'ref',
            'user',
            'client',
            'amount',
            'amount_cash',
            'shift',
            'date',
            'due_date',
            'status',
            'payment_date',
            'expenses'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'user_permissions': {'write_only': True},
            'groups': {'write_only': True}
        }
        depth = 1
