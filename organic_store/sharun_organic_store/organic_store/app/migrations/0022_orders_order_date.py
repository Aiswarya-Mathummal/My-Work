# Generated by Django 4.2.5 on 2023-10-16 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_cart_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
