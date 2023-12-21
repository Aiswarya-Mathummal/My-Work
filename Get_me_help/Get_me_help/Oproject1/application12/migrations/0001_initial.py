# Generated by Django 4.2.6 on 2023-10-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('reg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/')),
                ('usertype', models.IntegerField(default=2)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='service_center',
            fields=[
                ('center_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('usertype', models.IntegerField(default=3)),
            ],
        ),
    ]