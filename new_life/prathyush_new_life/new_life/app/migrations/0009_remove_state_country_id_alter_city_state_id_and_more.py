# Generated by Django 4.2.6 on 2023-10-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_state_country_id_alter_patient_details_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='country_id',
        ),
        migrations.AlterField(
            model_name='city',
            name='state_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='patient_details',
            name='status',
            field=models.CharField(choices=[('Picked Patient', 'Picked patient'), ('On the way', 'On the way'), ('Ride Completed', 'Ride Completed')], max_length=100),
        ),
    ]
