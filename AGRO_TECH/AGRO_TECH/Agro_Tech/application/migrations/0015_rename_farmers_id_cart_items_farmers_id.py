# Generated by Django 4.2.6 on 2023-10-26 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_rename_cart_id_cart_cart_id_rename_count_cart_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart_items',
            old_name='Farmers_Id',
            new_name='farmers_id',
        ),
    ]
