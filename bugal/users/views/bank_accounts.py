"""Bank Accounts views"""

# Django REST Framework
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Serializers
from bugal.users.serializers import BankAccountModelSerializer

# Models
from bugal.base.models import BankAccount

# Permissions
from ..permissions import IsAccountOwner


class BankAccountViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Bank Account view set."""
    serializer_class = BankAccountModelSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)
    
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
    
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = BankAccount.objects.filter(user=self.request.user)
        print("\nQry Obj: {0}\n".format(queryset))
        return queryset

    def perform_create(self, serializer):
        """Create a new Client."""
        serializer.save(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
