# Generated by Django 4.2.7 on 2023-11-16 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_offender_offence_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='offences',
            new_name='traffic_rules',
        ),
    ]
