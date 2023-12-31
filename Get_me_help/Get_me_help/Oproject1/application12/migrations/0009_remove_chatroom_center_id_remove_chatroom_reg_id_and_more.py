# Generated by Django 4.2.7 on 2023-11-12 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application12', '0008_chatroom_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatroom',
            name='center_id',
        ),
        migrations.RemoveField(
            model_name='chatroom',
            name='reg_id',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='chat_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='req_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application12.service_request'),
            preserve_default=False,
        ),
    ]
