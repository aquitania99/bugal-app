"""Guardians Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAccountOwner

# Serializers
from bugal.contacts.serializers import GuardianModelSerializer
from bugal.contacts.serializers import ContactInfoSerializer

# Models
from bugal.base.models import User, Guardian, Contact


class GuardianInfoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Guardian Info view set."""
    queryset = Guardian.objects.all()
    serializer_class = GuardianModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def perform_create(self, serializer):
        """Create a new Client."""
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        instance = Guardian.objects.filter(id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        """Update Client"""
        kwargs['partial'] = True
        instance = Guardian.objects.filter(id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        print("\nInstance: {0}\n".format(instance))
        print("\nValid: {0}\n".format(serializer.is_valid))
        serializer.save()

        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
