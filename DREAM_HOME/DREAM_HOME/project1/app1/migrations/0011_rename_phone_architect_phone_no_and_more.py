# Generated by Django 4.2.6 on 2023-10-17 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_architect_status_exterior_designer_status_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='architect',
            old_name='phone',
            new_name='phone_no',
        ),
        migrations.RenameField(
            model_name='exterior_designer',
            old_name='phone',
            new_name='phone_no',
        ),
    ]