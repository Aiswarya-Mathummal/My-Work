# Generated by Django 4.2.6 on 2023-10-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_customer_address_alter_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='architect',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='architect',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='exterior_designer',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='exterior_designer',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='interior_designer',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='interior_designer',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
