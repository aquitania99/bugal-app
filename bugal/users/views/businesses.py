"""Businesses Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Serializers
from bugal.users.serializers import BusinessInfoSerializer

# Models
from bugal.base.models import User, BusinessInfo


class BusinessInfoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Business Info view set."""
    serializer_class = BusinessInfoSerializer
    permission_classes = (IsAuthenticated,)

    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = BusinessInfo.objects.filter(user=self.request.user)
        return queryset    
    
    def perform_create(self, serializer):
        """Create a new Business record."""
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

