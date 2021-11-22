"""User views"""

# Django REST Framework
from bugal.base.models.banks import Bank
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, authentication

# Django Reset Password
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

# Permissions
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from bugal.users.permissions import IsAccountOwner

# Serializers
from bugal.users.serializers import (
    UserModelSerializer, UserSignUpSerializer, 
    UserLoginSerializer, AccountVerificationSerializer,
    BankAccountModelSerializer, BusinessInfoSerializer
)
from bugal.contacts.serializers import ContactModelSerializer, ContactInfoSerializer

# Models
from bugal.base.models import User, Contact, BankAccount, BusinessInfo


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """User view set.

    Handle sign up, login and account verification.
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'uuid'

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        
        user_data = UserModelSerializer(user).data
        
        usr = {
            'uid': user_data['uuid'],
            'email': user_data['email'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name']
        }
        
        data = {
            'user': usr,
            'access_token': token
        }

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # data = UserModelSerializer(user).data

        return Response(status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def verify(self, request):
        """Account verification."""
        serializer = AccountVerificationSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Your account is verified!'}
        return Response(data, status=status.HTTP_200_OK)

    # def destroy(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     self.save(request, *args, **kwargs)
        
    #     return Response({'success': True}, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        """Get all the user data."""
        data = self.get_user_details(request, *args, **kwargs)

        return Response(data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        businesses = BusinessInfo.objects.all()
        bank_accounts = BankAccount.objects.all()
        banks = Bank.objects.all()
        if request.data.__contains__('abn'):
            request.data['gst'] = 10 if request.data['is_taxable'] else 0
            request.data['terms'] = request.data['payment_terms']
            request.data.pop('is_taxable')
            request.data.pop('payment_terms')
            print("\nWill Create / Update ABN with: {0}\n".format(request.data))
            chk_abn, created = businesses.get_or_create(user=self.request.user)
            print("\nCHK_ABN: {0}\n".format(str(chk_abn)))
            if not chk_abn:
                update_business = BusinessInfoSerializer(BusinessInfo, data=request.data)
                update_business.is_valid(raise_exception=True)
                # print("ABN ADD PAYLOAD - IS VALID: {0}".format(update_business.is_valid()))
                update_business.save(user=self.request.user)
                # print("ABN ADD PAYLOAD - VALID DATA: {0}".format(update_business.validated_data))
            else:
                update_business = BusinessInfoSerializer(chk_abn, data=request.data)
                update_business.is_valid(raise_exception=True)
                # print("ABN UPDATE PAYLOAD - IS VALID: {0}".format(update_business.is_valid()))
                update_business.save(user=self.request.user)
                # print("ABN UPDATE PAYLOAD - VALID DATA: {0}".format(update_business.validated_data))
        
        if request.data.__contains__('bank_id'):
            print("Bank Account Data: {0}".format(request.data))
            # chk_account = banks.get(user=self.request.user.pk)
            chk_account = bank_accounts.filter(user=self.request.user.pk)
            print("\nCHK_BANK_ACCOUNT: {0}\n".format(chk_account))
            # request.data['user'] = self.request.user.pk
            bank, created = banks.get_or_create(id=request.data['bank_id'])
            request.data['bank'] = bank.id
            request.data['bsb'] = request.data['bank_bsb']
            request.data['number'] = int(request.data['bank_account'])
            request.data.pop('bank_id')
            request.data.pop('bank_bsb')
            request.data.pop('bank_account')
            # import pdb; pdb.set_trace()
            if not chk_account:
                update_bank_data = BankAccountModelSerializer(data=request.data)
                update_bank_data.is_valid(raise_exception=True)
                update_bank_data.save(user=self.request.user)
            else:
                update_bank_data = BankAccountModelSerializer(chk_account, data=request.data)
                update_bank_data.is_valid(raise_exception=True)
                update_bank_data.update(chk_account.get(), update_bank_data.validated_data)
        
        self.update(request, *args, **kwargs)
        
        data = self.get_user_details(request, *args, **kwargs)
        
        return Response(data, status=status.HTTP_200_OK)

    @receiver(reset_password_token_created)
    def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

        send_mail(
            # title:
            "Password Reset for {title}".format(title="Some website title"),
            # message:
            f"Password reset TOKEN: http://localhost:3000/verify/{reset_password_token.key}",
            # from:
            "noreply@somehost.local",
            # to:
            [reset_password_token.user.email]
        )

    def get_user_details(self, request, *args, **kwargs):
        """Add extra data to the response."""
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        clients = Contact.objects.filter(
            user=request.user,
            user__is_active=True
        )
        business = BusinessInfo.objects.filter(
            user=request.user,
            user__is_active=True
        )
        bank_account = BankAccount.objects.filter(
            user=request.user,
            user__is_active=True
        )
        data = {
            "user": response.data,
            "business": BusinessInfoSerializer(business, many=True).data,
            "clients": ContactInfoSerializer(clients, many=True).data,
            "bank_accounts": BankAccountModelSerializer(bank_account, many=True).data
        }
        
        return data

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserModelSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
