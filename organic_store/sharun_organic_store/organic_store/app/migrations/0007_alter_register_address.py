# Generated by Django 4.2.5 on 2023-10-08 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_register_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=100),
        ),
    ]