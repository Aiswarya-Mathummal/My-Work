# Generated by Django 4.2.6 on 2023-11-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_int_design_book_ext_design_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='blueprint',
            field=models.ImageField(blank=True, null=True, upload_to='blueprint/'),
        ),
    ]
