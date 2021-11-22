"""User Shifts Serializers"""

# Django REST Frameworks
from rest_framework import serializers

# Model
from bugal.base.models import Shift

# Serializers
from bugal.users.serializers import UserModelSerializer


class ShiftModelSerializer(serializers.ModelSerializer):
    """Shift model serializer"""

    class Meta:
        """Meta class."""

        model = Shift
        fields = (
            'id',
            'client',
            'shift',
            'shift_name',
            'shift_comment',
            'hourly_rate',
            'meet_date',
            'meet_time',
            'meet_duration',
            'meet_latitude',
            'meet_longitude',
            'notification_time',
            'repeat_shift',
            'current_shift',
            'status'
        )
        read_only_fields = ('user', 'client', 'shift')
        extra_kwargs = {
            'user_permissions': {'write_only': True},
        }
        depth = 1


