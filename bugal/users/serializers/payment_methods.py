"""Payment Methods Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import PaymentMethod


class PaymentMethodModelSerializer(serializers.ModelSerializer):
    """Payment method model serializer"""

    class Meta:
        """Meta class."""

        model = PaymentMethod
        fields = '__all__'

