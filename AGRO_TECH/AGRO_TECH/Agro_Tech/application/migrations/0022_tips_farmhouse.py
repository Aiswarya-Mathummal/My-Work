# Generated by Django 4.2.6 on 2023-11-08 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_alter_tips_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='farmhouse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.farmhouse_reg'),
            preserve_default=False,
        ),
    ]
