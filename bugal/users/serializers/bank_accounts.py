"""Bank Account Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import BankAccount
from bugal.base.models import User
from bugal.base.models import Bank

# Serializers
from bugal.users.serializers import UserModelSerializer


class BankAccountModelSerializer(serializers.ModelSerializer):
    """Bank Account model serializer"""
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """Meta class."""

        model = BankAccount
        fields = (
            'id',
            'user',
            'bank',
            'bsb',
            'number',
        )