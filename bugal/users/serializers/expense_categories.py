"""Expense Categories Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import ExpenseCategory


class ExpenseCategorySerializer(serializers.ModelSerializer):
    """Expense category model serializer"""

    class Meta:
        """Meta class."""

        model = ExpenseCategory
        fields = '__all__'

