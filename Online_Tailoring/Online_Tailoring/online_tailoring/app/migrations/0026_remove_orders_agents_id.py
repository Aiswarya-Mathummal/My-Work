# Generated by Django 4.2.6 on 2023-11-04 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_orders_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='agents_id',
        ),
    ]
