# Generated by Django 4.2.6 on 2023-10-26 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_rename_cart_id_cart_items_carts_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='Cart_Id',
            new_name='cart_id',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='Count',
            new_name='count',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='User_Id',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='cart_items',
            old_name='Carts_Id',
            new_name='carts_id',
        ),
        migrations.RenameField(
            model_name='cart_items',
            old_name='Item_Id',
            new_name='item_id',
        ),
        migrations.RenameField(
            model_name='cart_items',
            old_name='Product_Id',
            new_name='product_id',
        ),
        migrations.RenameField(
            model_name='cart_items',
            old_name='Qty',
            new_name='qty',
        ),
        migrations.RenameField(
            model_name='cart_items',
            old_name='User_Id',
            new_name='user_id',
        ),
    ]