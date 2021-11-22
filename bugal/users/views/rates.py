"""Businesses Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.settings import perform_import
# Serializers
from bugal.users.serializers import RateModelSerializer
# Models
from bugal.base.models import RateModel
# Permissions
from ..permissions import IsAccountOwner


class RateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Shift Type Info view set."""
    serializer_class = RateModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)
    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = RateModel.objects.all()
        return queryset    
    
    def retrieve(self, request, *args, **kwargs):
        """Get all the rate data."""
        instance = RateModel.objects.filter(user=self.request.user, id=kwargs['pk']).first()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        """Create a new Guardian record."""
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        instance = RateModel.objects.filter(user=self.request.user, id=kwargs['pk']).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, *args, **kwargs):
        """Delete Rate"""
        delete_rate = RateModel.objects.filter(user=self.request.user, id=kwargs['pk'])
        delete_rate.get()
        delete_rate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)