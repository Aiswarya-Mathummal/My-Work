# Generated by Django 4.2.6 on 2023-11-03 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_sewing_details_tailor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sewing_details',
            name='ordered_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]