# Generated by Django 4.2.6 on 2023-11-03 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_sewing_measurements_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sewing_details',
            name='fabric1_qty',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sewing_details',
            name='fabric2_qty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='sewing_details',
            name='fabric3_qty',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
