# Generated by Django 4.2.6 on 2023-10-28 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery_agent',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='agent_pic/'),
        ),
        migrations.AddField(
            model_name='designer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='designer_pic/'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='manufacturer_pic/'),
        ),
        migrations.AddField(
            model_name='tailor',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='tailor_pic/'),
        ),
    ]
