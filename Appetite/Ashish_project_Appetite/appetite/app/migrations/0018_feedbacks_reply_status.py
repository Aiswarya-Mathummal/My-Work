# Generated by Django 4.2.7 on 2023-11-09 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_complaints_reply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='reply_status',
            field=models.BooleanField(default=True),
        ),
    ]
