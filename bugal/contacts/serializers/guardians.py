"""Guardians Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import Guardian


class GuardianModelSerializer(serializers.ModelSerializer):
    """Client model serializer"""
    
    class Meta:
        """Meta class."""
        model = Guardian

        fields = (
            'id',
            'first_name',
            'last_name',
            'email'
        )

    def partial_update(self, validated_data):
        import pdb; pdb.set_trace()
        return Guardian.objects.update_or_create(**validated_data)
