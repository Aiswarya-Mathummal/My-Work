# Generated by Django 4.2.5 on 2023-10-13 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='customer',
        ),
        migrations.RenameModel(
            old_name='fuel_det',
            new_name='fuel_details',
        ),
    ]
