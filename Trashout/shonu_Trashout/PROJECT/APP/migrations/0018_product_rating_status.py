# Generated by Django 4.2.7 on 2023-11-15 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0017_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating_status',
            field=models.BooleanField(default=True),
        ),
    ]
