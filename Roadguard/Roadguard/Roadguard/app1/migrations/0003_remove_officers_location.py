# Generated by Django 4.2.7 on 2023-11-15 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_offences_offender_delete_offense_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officers',
            name='location',
        ),
    ]