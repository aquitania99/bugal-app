"""Bugal Utils Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import (
    Country, State, Gender
)


class CountryModelSerializer(serializers.ModelSerializer):
    """Country model serializer"""

    class Meta:
        """Meta class."""

        model = Country
        fields = (
            'id',
            'name',
            'short_name'
        )


class StateModelSerializer(serializers.ModelSerializer):
    """Country model serializer"""

    class Meta:
        """Meta class."""

        model = State
        fields = (
            'id',
            'name',
            'short_name'
        )


class GenderModelSerializer(serializers.ModelSerializer):
    """Gender model serializer"""

    class Meta:
        """Meta class."""

        model = Gender
        fields = (
            'id',
            'identity'
        )
