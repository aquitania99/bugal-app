"""Businesses Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Serializers
from bugal.users.serializers import PaymentMethodModelSerializer
# Models
from bugal.base.models import PaymentMethod
# Permissions
from ..permissions import IsAccountOwner


class PaymentMethodViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Shift Type Info view set."""
    serializer_class = PaymentMethodModelSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = PaymentMethod.objects.all()
        return queryset    
    
    def perform_create(self, serializer):
        """Create a new Guardian record."""
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

