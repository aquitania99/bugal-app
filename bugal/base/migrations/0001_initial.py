# Generated by Django 3.0.11 on 2020-11-02 13:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('NDISID', models.IntegerField(null=True, unique=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('dob', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('last_updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was created.', verbose_name='last updated at')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +9999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('address_unit', models.IntegerField(null=True)),
                ('address_number', models.IntegerField(null=True)),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_suburb', models.CharField(max_length=255, null=True)),
                ('address_state_id', models.IntegerField(null=True)),
                ('address_country_id', models.IntegerField(null=True)),
                ('address_postcode', models.CharField(max_length=5, null=True)),
                ('address_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address_lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('timezone', models.CharField(max_length=45, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=255, unique=True, verbose_name='email address')),
                ('is_verified', models.BooleanField(default=False, help_text='Set to true when the user have verified its email address.', verbose_name='verified')),
                ('is_active', models.BooleanField(default=True, help_text='Set to true by default when the user is created', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Set to false by default when the user is created', verbose_name='staff')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='bank short name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='bank name')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('NDISID', models.IntegerField(null=True, unique=True)),
                ('dob', models.DateField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('last_updated', models.DateTimeField(auto_now=True, help_text='Date time on which the object was created.', verbose_name='last updated at')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +9999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('address_unit', models.IntegerField(null=True)),
                ('address_number', models.IntegerField(null=True)),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_suburb', models.CharField(max_length=255, null=True)),
                ('address_state_id', models.IntegerField(null=True)),
                ('address_country_id', models.IntegerField(null=True)),
                ('address_postcode', models.CharField(max_length=5, null=True)),
                ('address_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address_lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('timezone', models.CharField(max_length=45, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('client', 'client'), ('organisation', 'organisation'), ('guardian', 'guardian')], max_length=20)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('org_name', models.CharField(max_length=255, null=True)),
                ('address_line', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'A record with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'ordering': ['-date_created', '-last_updated'],
                'get_latest_by': 'date_created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('short_name', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='expense name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='expense description')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say'), ('N/A', 'N/A')], default='N/A', max_length=20, unique=True)),
                ('description', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +9999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('address_unit', models.IntegerField(null=True)),
                ('address_number', models.IntegerField(null=True)),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_suburb', models.CharField(max_length=255, null=True)),
                ('address_state_id', models.IntegerField(null=True)),
                ('address_country_id', models.IntegerField(null=True)),
                ('address_postcode', models.CharField(max_length=5, null=True)),
                ('address_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address_lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('timezone', models.CharField(max_length=45, null=True)),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('dob', models.DateField(null=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='payment method name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='payment method description')),
            ],
        ),
        migrations.CreateModel(
            name='ShiftType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='shift type')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('short_name', models.CharField(max_length=5, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(blank=True, max_length=50, null=True)),
                ('shift_comment', models.CharField(blank=True, max_length=255, null=True)),
                ('hourly_rate', models.IntegerField(blank=True, null=True)),
                ('meet_date', models.DateField(blank=True, null=True)),
                ('meet_time', models.TimeField(blank=True, null=True)),
                ('meet_duration', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('meet_latitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('meet_longitude', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('notification_time', models.DateTimeField(blank=True, null=True)),
                ('repeat_shift', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('current_shift', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Finalised', 'Finalised'), ('Pending', 'Pending')], default='Pending', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Contact')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.ShiftType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='rate name')),
                ('hourly', models.DecimalField(decimal_places=2, max_digits=6)),
                ('detail', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +9999999999. Up to 15 digits allowed.', regex='\\+?1?\\d{9,15}$')])),
                ('address_unit', models.IntegerField(null=True)),
                ('address_number', models.IntegerField(null=True)),
                ('address_street', models.CharField(max_length=255, null=True)),
                ('address_suburb', models.CharField(max_length=255, null=True)),
                ('address_state_id', models.IntegerField(null=True)),
                ('address_country_id', models.IntegerField(null=True)),
                ('address_postcode', models.CharField(max_length=5, null=True)),
                ('address_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('address_lon', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('timezone', models.CharField(max_length=45, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(blank=True, max_length=12, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('amount_cash', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('SE', 'SavedExit'), ('SS', 'SavedSent'), ('U', 'Unpaid'), ('P', 'Paid'), ('WO', 'WriteOff')], default='', max_length=3, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('rate_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='rate name')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Contact')),
                ('shift', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Shift')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('attachment_url', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.ExpenseCategory')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Contact')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.PaymentMethod')),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Shift')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Gender'),
        ),
        migrations.AddField(
            model_name='contact',
            name='guardian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Guardian'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='BusinessInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abn', models.BigIntegerField(null=True, unique=True)),
                ('gst', models.PositiveIntegerField(blank=True, null=True)),
                ('terms', models.PositiveIntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bsb', models.PositiveIntegerField(default=0)),
                ('number', models.PositiveIntegerField(default=0)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Bank')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]