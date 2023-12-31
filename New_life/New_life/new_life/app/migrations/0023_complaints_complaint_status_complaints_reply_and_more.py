# Generated by Django 4.2.6 on 2023-10-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_ambulance_drivers_district_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='complaint_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='reply',
            field=models.TextField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaints',
            name='reply_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking_details',
            name='driver_status',
            field=models.CharField(choices=[('Ride Completed', 'Ride Completed'), ('Picked Patient', 'Picked Patient'), ('Ride In Progress', 'Ride In Progress'), ('Ride Started', 'Ride Started')], default='Driver Assigned', max_length=100),
        ),
    ]
