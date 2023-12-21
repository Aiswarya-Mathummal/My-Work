# Generated by Django 4.2.5 on 2023-10-29 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_fuel_request_bunkid_fuel_request_fuelid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fuel_request',
            name='fuel_type',
        ),
        migrations.AddField(
            model_name='fuel_request',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=11, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuel_request',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=11, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuel_request',
            name='req_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='bunk_location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('bunk_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.petrol_bunk')),
            ],
        ),
    ]
