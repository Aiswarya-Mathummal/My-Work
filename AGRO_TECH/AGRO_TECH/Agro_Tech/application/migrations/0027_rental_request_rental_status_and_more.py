# Generated by Django 4.2.6 on 2023-11-12 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0026_alter_rental_request_req_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental_request',
            name='rental_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rental_request',
            name='req_status',
            field=models.BooleanField(default=True),
        ),
    ]