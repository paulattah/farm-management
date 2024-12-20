# Generated by Django 5.0.2 on 2024-11-25 08:00

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairy', '0004_alter_semen_date_of_expiry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semen',
            name='date_of_expiry',
            field=models.DateField(error_messages={'min_value': 'Invalid date entry, Date of expiry must be in future'}, validators=[django.core.validators.MinValueValidator(datetime.date(2024, 11, 25))]),
        ),
        migrations.AlterField(
            model_name='semen',
            name='date_of_production',
            field=models.DateField(error_messages={'max_value': 'Invalid date entry, Dates of production must not be in future'}, validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 11, 25))]),
        ),
        migrations.AlterField(
            model_name='symptoms',
            name='date_observed',
            field=models.DateField(error_messages={'max_value': 'The date of observation cannot be in the future!.'}, validators=[django.core.validators.MaxValueValidator(datetime.date(2024, 11, 25))]),
        ),
    ]
