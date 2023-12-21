# Generated by Django 4.2.7 on 2023-11-07 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_register_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='surplus_requests',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('accepted_on', models.DateTimeField(auto_now_add=True)),
                ('pickup_at', models.CharField(default='', max_length=100)),
                ('pickup_status', models.BooleanField(default=False)),
                ('delivered_at', models.CharField(default='', max_length=100)),
                ('deliver_status', models.BooleanField(default=False)),
                ('request_status', models.BooleanField(default=True)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.delivery_agent')),
                ('surplus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.supplier_surplus_food')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.register')),
            ],
        ),
    ]
