# Generated by Django 4.2.6 on 2023-10-29 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='designs',
            fields=[
                ('design_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='design_images/')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('designer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.designer')),
            ],
        ),
    ]
