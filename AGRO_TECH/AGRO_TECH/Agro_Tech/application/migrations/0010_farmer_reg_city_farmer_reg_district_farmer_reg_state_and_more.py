# Generated by Django 4.2.6 on 2023-10-23 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_remove_user_reg_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer_reg',
            name='City',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer_reg',
            name='District',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer_reg',
            name='State',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmhouse_reg',
            name='City',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmhouse_reg',
            name='District',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmhouse_reg',
            name='State',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_reg',
            name='City',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_reg',
            name='District',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_reg',
            name='State',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
