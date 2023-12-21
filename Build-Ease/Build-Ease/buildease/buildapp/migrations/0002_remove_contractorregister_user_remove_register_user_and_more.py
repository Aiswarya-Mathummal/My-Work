# Generated by Django 4.2.6 on 2023-10-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractorregister',
            name='User',
        ),
        migrations.RemoveField(
            model_name='register',
            name='User',
        ),
        migrations.RemoveField(
            model_name='workerregister',
            name='User',
        ),
        migrations.AddField(
            model_name='contractorregister',
            name='User_Type',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='register',
            name='User_Type',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='workerregister',
            name='User_Type',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='contractorregister',
            name='district',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workerregister',
            name='district',
            field=models.CharField(max_length=100),
        ),
    ]
