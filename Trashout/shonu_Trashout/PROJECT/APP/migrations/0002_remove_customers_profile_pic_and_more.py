# Generated by Django 4.2.6 on 2023-10-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='recyling_unit',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customers',
            name='id_proof',
            field=models.ImageField(blank=True, null=True, upload_to='id_proof/'),
        ),
        migrations.AddField(
            model_name='recyling_unit',
            name='id_proof',
            field=models.ImageField(blank=True, null=True, upload_to='id_proof/'),
        ),
    ]
