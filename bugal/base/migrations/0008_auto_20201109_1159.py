# Generated by Django 3.0.11 on 2020-11-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_contact_soft_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='has_guardian',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contact',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Other family member', 'Other family member'), ('Friend', 'Friend'), ('Legal Guardian', 'Legal Guardian'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]