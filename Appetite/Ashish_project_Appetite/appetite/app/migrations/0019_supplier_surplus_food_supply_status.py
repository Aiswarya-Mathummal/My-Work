# Generated by Django 4.2.7 on 2023-11-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_feedbacks_reply_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier_surplus_food',
            name='supply_status',
            field=models.BooleanField(default=False),
        ),
    ]
