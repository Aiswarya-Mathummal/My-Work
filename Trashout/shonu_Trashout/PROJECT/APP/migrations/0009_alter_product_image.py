# Generated by Django 4.2.6 on 2023-11-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_i mages/'),
        ),
    ]