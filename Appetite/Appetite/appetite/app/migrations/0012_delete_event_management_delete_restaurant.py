# Generated by Django 4.2.7 on 2023-11-07 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_restaurant_surplus_food_restaurant_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='event_management',
        ),
        migrations.DeleteModel(
            name='restaurant',
        ),
    ]
