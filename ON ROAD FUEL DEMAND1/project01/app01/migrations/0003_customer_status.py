# Generated by Django 4.2.5 on 2023-10-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_rename_signup_customer_rename_fuel_det_fuel_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
