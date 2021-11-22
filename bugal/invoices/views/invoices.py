"""Invoice views"""
# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Serializers
from bugal.invoices.serializers import InvoiceModelSerializer

# Models
from bugal.base.models import  Contact, Invoice

# Permissions
from ..permissions import IsAccountOwner


class InvoiceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Client view set."""
    queryset = Invoice.objects.all()
    serializer_class = InvoiceModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        queryset = Invoice.objects.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        instance = Contact.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        """Create a new Client."""
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        """Update Invoice"""
        instance = Invoice.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        print("\nInstance: {0}\n".format(instance))
        print("\nValid: {0}\n".format(serializer.is_valid))
        serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

