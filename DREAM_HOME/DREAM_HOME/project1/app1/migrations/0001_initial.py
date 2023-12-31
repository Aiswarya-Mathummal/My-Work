# Generated by Django 4.2.6 on 2023-10-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Architect',
            fields=[
                ('architect_id', models.AutoField(primary_key=True, serialize=False)),
                ('architect_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.DateField(auto_now=True)),
                ('place', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
                ('experience', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.DateField(auto_now=True)),
                ('place', models.CharField(max_length=50)),
                ('post', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('district', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone_no', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo/')),
            ],
        ),
    ]
