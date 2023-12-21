# Generated by Django 4.2.7 on 2023-11-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_restaurant_surplus_food_timeexpire_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='surplus_food_supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True)),
                ('phone_no', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='restaurant_pic/')),
                ('id', models.ImageField(blank=True, null=True, upload_to='restaurant_id/')),
                ('usertype', models.IntegerField(default=3)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
