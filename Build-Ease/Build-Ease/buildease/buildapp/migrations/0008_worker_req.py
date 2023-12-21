# Generated by Django 4.2.6 on 2023-10-26 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildapp', '0007_previous_designs'),
    ]

    operations = [
        migrations.CreateModel(
            name='worker_req',
            fields=[
                ('ReqId', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Status', models.BooleanField(default=False)),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildapp.register')),
                ('workId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildapp.work')),
                ('workerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildapp.workerregister')),
            ],
        ),
    ]
