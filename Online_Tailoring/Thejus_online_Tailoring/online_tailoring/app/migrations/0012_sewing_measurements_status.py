# Generated by Django 4.2.6 on 2023-11-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_sewing_request_requested_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='sewing_measurements',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]