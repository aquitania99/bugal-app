"""Rates Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import RateModel, User

# Serializers
from .users import UserModelSerializer


class RateModelSerializer(serializers.ModelSerializer):
    """Rate model serializer"""
    class Meta:
        """Meta class."""

        model = RateModel
        fields = '__all__'
        read_only_fields = ('id', 'user')
