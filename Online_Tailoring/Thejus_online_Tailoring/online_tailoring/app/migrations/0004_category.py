# Generated by Django 4.2.6 on 2023-10-29 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_delivery_agent_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
    ]
