# Generated by Django 4.2.7 on 2023-11-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_offences_reporter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='offences',
            name='user_status',
            field=models.BooleanField(default=False),
        ),
    ]
