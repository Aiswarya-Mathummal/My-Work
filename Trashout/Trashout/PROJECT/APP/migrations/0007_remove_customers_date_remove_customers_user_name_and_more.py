# Generated by Django 4.2.6 on 2023-10-25 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_recycling_unit_unit_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='date',
        ),
        migrations.RemoveField(
            model_name='customers',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='recycling_unit',
            name='date',
        ),
        migrations.RemoveField(
            model_name='recycling_unit',
            name='user_name',
        ),
    ]
