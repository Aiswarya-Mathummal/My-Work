# Generated by Django 4.2.7 on 2023-11-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_officers_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offender',
            name='offence_id',
        ),
    ]
