# Generated by Django 4.2.7 on 2023-11-14 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0013_product_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_request',
            name='product_id',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='APP.product'),
            preserve_default=False,
        ),
    ]
