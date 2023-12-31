# Generated by Django 4.2.7 on 2023-11-09 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application12', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('state_id', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service_center',
            name='id',
            field=models.ImageField(blank=True, null=True, upload_to='service_center_id/'),
        ),
        migrations.CreateModel(
            name='service_request',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('vehicle_type', models.CharField(max_length=100)),
                ('req_status', models.BooleanField(default=False)),
                ('center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application12.register')),
                ('reg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application12.service_center')),
            ],
        ),
        migrations.CreateModel(
            name='service_center_location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application12.service_center')),
            ],
        ),
    ]
