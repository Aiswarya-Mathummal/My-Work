# Generated by Django 4.2.5 on 2023-10-25 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_alter_customer_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuel_details',
            name='Rate',
            field=models.FloatField(default=2),
        ),
    ]