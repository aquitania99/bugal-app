# Generated by Django 3.0.11 on 2020-11-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20201103_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='soft_deleted',
            field=models.BooleanField(default=False),
        ),
    ]