# Generated by Django 4.2.6 on 2023-11-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_sewing_measurements_sleeve_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sewing_measurements',
            name='status',
        ),
        migrations.AddField(
            model_name='sewing_request',
            name='measurement_status',
            field=models.BooleanField(default=False),
        ),
    ]
