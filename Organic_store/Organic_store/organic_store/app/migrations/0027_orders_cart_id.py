# Generated by Django 4.2.5 on 2023-10-16 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_delivery_agent_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cart_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cart'),
            preserve_default=False,
        ),
    ]
