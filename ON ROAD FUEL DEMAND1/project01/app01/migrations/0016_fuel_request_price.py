# Generated by Django 4.2.6 on 2023-11-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_rename_fuelid_fuel_request_fuel_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_request',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
