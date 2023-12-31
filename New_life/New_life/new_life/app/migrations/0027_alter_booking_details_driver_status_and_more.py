# Generated by Django 4.2.6 on 2023-10-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_patient_details_latitude_patient_details_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_details',
            name='driver_status',
            field=models.CharField(choices=[('Ride In Progress', 'Ride In Progress'), ('Ride Completed', 'Ride Completed'), ('Picked Patient', 'Picked Patient'), ('Ride Started', 'Ride Started')], default='Driver Assigned', max_length=100),
        ),
        migrations.AlterField(
            model_name='driver_location',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver_location',
            name='longitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='latitude',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='longitude',
            field=models.IntegerField(),
        ),
    ]
