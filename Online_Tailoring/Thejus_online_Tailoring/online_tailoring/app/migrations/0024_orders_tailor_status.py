# Generated by Django 4.2.6 on 2023-11-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_remove_sewing_details_ordered_on_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='tailor_status',
            field=models.CharField(default='Requested Manufactures For Fabrics', max_length=100),
        ),
    ]
