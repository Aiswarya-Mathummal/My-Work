# Generated by Django 4.2.6 on 2023-11-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_sewing_measurements_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewing_measurements',
            name='sleeve_length',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
