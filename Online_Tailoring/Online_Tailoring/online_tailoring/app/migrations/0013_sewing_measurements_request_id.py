# Generated by Django 4.2.6 on 2023-11-02 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_sewing_measurements_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='sewing_measurements',
            name='request_id',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='app.sewing_request'),
            preserve_default=False,
        ),
    ]