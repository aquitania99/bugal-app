"""Expenses Info views"""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Serializers
from bugal.users.serializers import ExpenseSerializer

# Models
from bugal.base.models import Expense, ExpenseCategory, PaymentMethod
# Permissions
from ..permissions import IsAccountOwner


class ExpenseViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """Expense Info view set."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (IsAuthenticated, IsAccountOwner)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        print("\nObj: {0}\n".format(self.request.user))
        queryset = Expense.objects.filter(user=self.request.user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to the response."""
        print("Putazo! \n{0}\n{1}\n".format(self.request.user, int(kwargs['pk'])))
        instance = Expense.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        """Create a new Expense record."""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        """Update User Expense"""
        print("\nUSER: {0}".format(self.request.user))
        print("\nPK: {0}".format(int(kwargs['pk'])))
        instance = Expense.objects.filter(user=self.request.user, id=int(kwargs['pk'])).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        print("\nInstance: {0}\n".format(instance))
        print("\nValid: {0}\n".format(serializer.is_valid))
        serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)

