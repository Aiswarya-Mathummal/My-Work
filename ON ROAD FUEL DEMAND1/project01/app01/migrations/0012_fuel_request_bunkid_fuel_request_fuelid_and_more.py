# Generated by Django 4.2.5 on 2023-10-27 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_city_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuel_request',
            name='bunkid',
            field=models.ForeignKey(default=34567890, on_delete=django.db.models.deletion.CASCADE, to='app01.petrol_bunk'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuel_request',
            name='fuelid',
            field=models.ForeignKey(default=98765432, on_delete=django.db.models.deletion.CASCADE, to='app01.fuel_details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuel_request',
            name='userid',
            field=models.ForeignKey(default=34567, on_delete=django.db.models.deletion.CASCADE, to='app01.customer'),
            preserve_default=False,
        ),
    ]
