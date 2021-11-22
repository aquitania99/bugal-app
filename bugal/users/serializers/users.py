"""Users serializers"""

# Django
from django.conf import settings
from django.contrib.auth import get_user_model, password_validation, authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from bugal.base.models import User

# Serializers
from bugal.contacts.serializers import ContactModelSerializer
# from .businesses import BusinessInfoSerializer
# from .bank_accounts import BankAccountModelSerializer

# Utilities
import jwt
from datetime import timedelta
import pdb


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer"""
    client = ContactModelSerializer(many=True, read_only=True)
    # business = BusinessInfoSerializer(many=True)
    # bank = BankAccountModelSerializer(many=True)

    class Meta:
        """Meta class"""
        model = User
        
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
                'min_length': 8
            },
            'user_permissions': {'write_only': True},
            'groups': {'write_only': True}
        }


class UserLoginSerializer(serializers.Serializer):
    """User login serializer.

    Handle the login request data.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify credentials."""
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_verified:
            raise serializers.ValidationError('Account is not active yet =(')
        self.context['user'] = user
        return data

    def get_tokens_for_user(self, data):
        refresh = RefreshToken.for_user(data)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, data):
        """Generate or retrieve new token."""
        # token, created = Token.objects.get_or_create(user=self.context['user'])
        token = self.get_tokens_for_user(self.context['user'])
        return self.context['user'], token

    def update(self, instance, validated_data):
        """Update a user, setting password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user
    
    
class UserSignUpSerializer(serializers.Serializer):
    """"User sign up serializer.

    Handle sign up data validation
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    # password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        password_validation.validate_password(passwd)
        return data
    
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = get_user_model().objects.create_user(**validated_data)
        self.send_confirmation_email(user)
        return user
    
    def update(self, instance, validated_data):
        """Update a user, setting password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

    def send_confirmation_email(self, user):
        """Send account verification link to given user."""
        verification_token = self.gen_verification_token(user)
        subject = "Welcome @{}! Verify your account to start using Bugal"
        from_email = 'verify <info@akela.solutions>'
        content = render_to_string(
            'emails/users/account_verification.html',
            {'token': verification_token, 'user': user}
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
        print("Sending email!")

    @staticmethod
    def gen_verification_token(user):
        """Create JWT token that the user can use to verify its account"""
        exp_date = timezone.now() + timedelta(days=1)
        payload = {
            'user': user.email,
            'exp': int(exp_date.timestamp()),
            'type': 'email_confirmation'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        return token.decode()


class AccountVerificationSerializer(serializers.Serializer):
    """Account verification serializer"""

    token = serializers.CharField()

    def validate_token(self, data):
        """Verify token is valid"""
        try:
            payload = jwt.decode(data, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise serializers.ValidationError('Verification link has expired.')
        except jwt.PyJWTError:
            raise serializers.ValidationError('invalid token')
        if payload['type'] != 'email_confirmation':
            raise serializers.ValidationError('Invalid token')

        self.context['payload'] = payload
        return data

    def save(self):
        """Update user's verified status"""
        payload = self.context['payload']
        user = User.objects.get(email=payload['user'])
        user.is_verified = True
        user.save()


class UserResetPassword(serializers.Serializer):

    """Handles password reset."""
    
    def send_confirmation_email(self, user):
        """Send account verification link to given user."""
        reset_token = self.gen_password_reset_token(user)
        subject = "Hi @{}! You have requested a password reset"
        from_email = 'reset <info@akela.solutions>'
        content = render_to_string(
            'emails/users/password_reset.html',
            {'token': reset_token, 'user': user}
        )
        msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
        msg.attach_alternative(content, "text/html")
        msg.send()
        print("Sending email!")

    def gen_password_reset(self, user):
        """Create JWT token that the user can use to verify its account"""
        exp_date = timezone.now() + timedelta(minute=5)
        payload = {
            'user': user.email,
            'exp': int(exp_date.timestamp()),
            'type': 'password_reset'
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        print('\nToken: %s\n' % token.decode())
        return token.decode()
