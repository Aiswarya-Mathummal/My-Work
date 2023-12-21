# Generated by Django 4.2.6 on 2023-10-30 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_materials'),
    ]

    operations = [
        migrations.CreateModel(
            name='sewing_measurements',
            fields=[
                ('measurement_id', models.AutoField(primary_key=True, serialize=False)),
                ('brand_size', models.CharField(max_length=100)),
                ('chest_measurement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('waist_measurement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hip_measurement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shoulder_measurement', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sleeve_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outseam_length', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sewing_request',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('request_status', models.BooleanField(default=False)),
                ('design_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.designs')),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materials')),
                ('tailor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tailor')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register')),
            ],
        ),
        migrations.CreateModel(
            name='sewing_details',
            fields=[
                ('sewing_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('ordered_on', models.DateField(auto_now_add=True, null=True)),
                ('tailor_status', models.CharField(default='Waiting For The Fabrics', max_length=100)),
                ('sewing_status', models.BooleanField(default=False)),
                ('measurement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sewing_measurements')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sewing_request')),
            ],
        ),
    ]
