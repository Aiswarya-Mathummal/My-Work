# Generated by Django 4.2.6 on 2023-10-15 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_user_reg_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='Status',
        ),
    ]