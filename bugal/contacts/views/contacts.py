"""Conatct views"""
# Django REST Framework
import uuid
from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Serializers
from bugal.contacts.serializers import ContactInfoSerializer, ContactModelSerializer

# Models
from bugal.base.models import Contact, Guardian

# Permissions
from ..permissions import IsAccountOwner


class ContactViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Contact view set."""
    queryset = Contact.objects.all()
    serializer_class = ContactModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        queryset = Contact.objects.filter(user=self.request.user, soft_deleted=False)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        instance = get_object_or_404(Contact, user=self.request.user, uuid=kwargs['pk'], soft_deleted=False)
        serializer = ContactModelSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        """Create a new Contact."""
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        """Update Contact"""
        instance = get_object_or_404(Contact, user=self.request.user, uuid=kwargs['pk'], soft_deleted=False)
        serializer = ContactModelSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        print("\nUUID: {0}".format(instance))
        print("Valid: {0}".format(serializer.is_valid()))
        serializer.save(user=self.request.user)
        print("Validated Data: {0}\n".format(serializer.validated_data))

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        """Delete Contact"""
        get_contact = get_object_or_404(Contact, user=self.request.user, uuid=kwargs['pk'], soft_deleted=False)
        get_contact.soft_deleted = True
        serializer = ContactModelSerializer(get_contact).data
        soft_delete = ContactModelSerializer(Contact, data=serializer, partial=True)
        import pdb; pdb.set_trace()
    #     Contact.objects.update(**serializer)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
