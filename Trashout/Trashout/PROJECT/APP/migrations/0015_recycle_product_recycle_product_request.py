# Generated by Django 4.2.7 on 2023-11-14 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0014_product_request_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='recycle_product',
            fields=[
                ('rc_product_id', models.AutoField(primary_key=True, serialize=False)),
                ('uploaded_on', models.DateField(auto_now_add=True)),
                ('product_status', models.BooleanField(default=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.product')),
            ],
        ),
        migrations.CreateModel(
            name='recycle_product_request',
            fields=[
                ('req_id', models.AutoField(primary_key=True, serialize=False)),
                ('accepted_on', models.DateField(auto_now_add=True)),
                ('accept_status', models.BooleanField(default=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.customers')),
                ('rc_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.recycle_product')),
                ('recycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='APP.recycling_unit')),
            ],
        ),
    ]
