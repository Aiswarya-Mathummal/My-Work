# Generated by Django 4.2.7 on 2023-11-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_delete_event_management_delete_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surplus_food_supplier',
            name='id',
            field=models.ImageField(blank=True, null=True, upload_to='supplier_id/'),
        ),
        migrations.AlterField(
            model_name='surplus_food_supplier',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='supplier_pic/'),
        ),
    ]
