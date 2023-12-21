# Generated by Django 4.2.6 on 2023-11-04 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_remove_sewing_details_rate_given_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sewing_details',
            name='ordered_on',
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(blank=True, null=True)),
                ('deliver_status', models.BooleanField(default=False)),
                ('agents_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.delivery_agent')),
                ('sewing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sewing_details')),
            ],
        ),
    ]
