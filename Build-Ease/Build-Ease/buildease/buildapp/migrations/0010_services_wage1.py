# Generated by Django 4.2.6 on 2023-10-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildapp', '0009_services_delete_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='Wage1',
            field=models.FloatField(default=11, max_length=10),
            preserve_default=False,
        ),
    ]
