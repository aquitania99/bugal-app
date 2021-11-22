"""Businesses Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Serializers
from bugal.users.serializers import ShiftModelSerializer, ShiftTypeModelSerializer
# Models
from bugal.base.models import Shift, ShiftType
# Permissions
from ..permissions import IsAccountOwner


class ShiftInfoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Shift Info view set."""
    serializer_class = ShiftModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = Shift.objects.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        print("Putazo! \n{0}\n{1}\n".format(self.request.user, int(kwargs['pk'])))
        instance = Shift.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        """Create a new Guardian record."""
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        """Update Client"""
        print("\nUSER: {0}".format(self.request.user))
        print("\nPK: {0}".format(int(kwargs['pk'])))
        instance = Shift.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        print("\nInstance: {0}\n".format(instance))
        print("\nValid: {0}\n".format(serializer.is_valid))
        serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)


class ShiftTypeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Shift Type Info view set."""
    serializer_class = ShiftTypeModelSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        # queryset = Guardian.objects.filter(user=self.request.user)
        queryset = ShiftType.objects.all()
        return queryset    
    
    def perform_create(self, serializer):
        """Create a new Guardian record."""
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

