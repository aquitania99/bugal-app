"""Business Info Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import BusinessInfo
# Serializers
from bugal.users.serializers import UserModelSerializer


class BusinessInfoSerializer(serializers.ModelSerializer):
    """Business info model serializer"""
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        """Meta class."""

        model = BusinessInfo
        fields = (
            'id',
            'user',
            'abn',
            'gst',
            'terms'
        )
