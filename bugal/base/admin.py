# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _  # For multi-language projects, translate

# Models
from .models import *


class CustomUserAdmin(BaseUserAdmin):
    """User model admin"""
    ordering = ['id']
    list_display = ['uuid', 'email', 'first_name', 'last_name', 'is_verified', 'is_superuser']
    readonly_fields = ['uuid']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'uuid', )}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'is_verified',)}),
        (_('Address'), 
            {'fields': (
                'address_unit', 
                'address_number', 
                'address_street',
                'address_suburb',
                'address_state_id',
                'address_postcode',
                'address_country_id',
            )}
        ),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    list_filter = ('is_staff', 'last_updated')


@admin.register(Contact)
class ClientAdmin(admin.ModelAdmin):
    """Client model admin"""
    list_display = ('email', 'first_name', 'last_name', 'NDISID', 'phone_number')
    search_fields = ('email', 'first_name', 'last_name', 'guardian')
    list_filter = ('NDISID',)


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    """Bank model admin."""
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    """User bank account model admin."""
    list_display = ('bsb', 'number')
    search_fields = ('user__email', 'bank__name', 'number')
    list_filter = ('bank__name', 'user__email',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Country model admin."""
    list_display = ('id', 'name', 'short_name')
    search_fields = ('name', 'short_name')
    list_filter = ('name', 'short_name')


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """State model admin."""
    list_display = ('id', 'name', 'short_name')
    search_fields = ('name', 'short_name')
    list_filter = ('name', 'short_name')


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """State model admin."""
    list_display = ('id', 'identity')


admin.site.register(User, CustomUserAdmin)
