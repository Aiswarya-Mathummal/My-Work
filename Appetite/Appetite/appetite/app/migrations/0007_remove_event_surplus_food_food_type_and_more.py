# Generated by Django 4.2.7 on 2023-11-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_restaurant_surplus_food_food_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_surplus_food',
            name='food_type',
        ),
        migrations.AddField(
            model_name='event_surplus_food',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurant_surplus_food',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
