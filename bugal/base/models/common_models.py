"""Django models utilities"""

# Django
from django.db import models
from django.core.validators import RegexValidator


class BugalCommonUserModel(models.Model):
    """Custom user model that supports using email instead of user name"""
    # username = models.CharField(max_length=255, null=True)
    NDISID = models.IntegerField(null=True, unique=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)
    dob = models.DateField(null=True)
    date_created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    last_updated = models.DateTimeField(
        'last updated at',
        auto_now=True,
        help_text='Date time on which the object was created.'
    )

    class Meta:
        """Meta option"""

        abstract = True

        get_latest_by = 'date_created'
        ordering = ['-date_created', '-last_updated']


class CommonPhoneAddress(models.Model):
    """Common fields for Address and Phone"""
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +9999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address_unit = models.IntegerField(null=True)
    address_number = models.IntegerField(null=True)
    address_street = models.CharField(max_length=255, null=True)
    address_suburb = models.CharField(max_length=255, null=True)
    address_state_id = models.IntegerField(null=True)
    address_country_id = models.IntegerField(null=True)
    address_postcode = models.CharField(max_length=5, null=True)
    address_lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    address_lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    timezone = models.CharField(max_length=45, null=True)

    class Meta:
        """Meta option"""

        abstract = True
