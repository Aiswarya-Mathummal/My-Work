# Generated by Django 4.2.5 on 2023-10-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_cart_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
