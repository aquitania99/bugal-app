"""User Expenses Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    """Expense model serializer"""

    class Meta:
        """Meta class."""

        model = Expense
        fields = (
            'id',
            'shift',
            'user',
            'client',
            'category',
            'date',
            'amount',
            'payment_method',
            'attachment_url'
        )
        read_only_fields = ('user', 'client', 'shift', 'payment_method')
        extra_kwargs = {
            'user_permissions': {'write_only': True},
        }
