# Generated by Django 4.2.6 on 2023-11-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_alter_govt_policies_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_agent',
            name='usertype',
            field=models.IntegerField(default=5),
        ),
    ]