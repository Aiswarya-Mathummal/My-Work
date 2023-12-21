# Generated by Django 4.2.6 on 2023-11-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildapp', '0018_alter_worker_req_status_worker_maintence'),
    ]

    operations = [
        migrations.CreateModel(
            name='contractor_maintence',
            fields=[
                ('MaintenanceId', models.AutoField(primary_key=True, serialize=False)),
                ('contarctor_maintenance_image', models.ImageField(blank=True, null=True, upload_to='contarctor_maintenance/')),
                ('Status', models.BooleanField(default=True)),
                ('ReqId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildapp.contractor_req')),
            ],
        ),
    ]