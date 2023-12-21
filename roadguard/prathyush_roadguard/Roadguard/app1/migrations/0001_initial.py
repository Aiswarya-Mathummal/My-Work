# Generated by Django 4.2.6 on 2023-11-10 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='offense',
            fields=[
                ('offense_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('fine', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='offense_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('officer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=255)),
                ('station', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('id_proof', models.ImageField(blank=True, null=True, upload_to='officer_id/')),
                ('User_type', models.IntegerField(default=3)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=128)),
                ('User_type', models.IntegerField(default=2)),
                ('status', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('id', models.ImageField(blank=True, null=True, upload_to='user_id/')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle_details',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_no', models.CharField(max_length=17, unique=True)),
                ('vehicle_status', models.BooleanField(default=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='vehicle_details/')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.register')),
            ],
        ),
    ]
