"""Shift Types Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import ShiftType


class ShiftTypeModelSerializer(serializers.ModelSerializer):
    """Shift type model serializer"""

    class Meta:
        """Meta class."""

        model = ShiftType
        fields = '__all__'

