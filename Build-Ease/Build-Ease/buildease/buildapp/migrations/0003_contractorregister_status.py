# Generated by Django 4.2.6 on 2023-10-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildapp', '0002_remove_contractorregister_user_remove_register_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorregister',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
