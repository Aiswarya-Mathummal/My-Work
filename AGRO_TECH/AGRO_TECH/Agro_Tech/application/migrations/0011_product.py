# Generated by Django 4.2.6 on 2023-10-23 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_farmer_reg_city_farmer_reg_district_farmer_reg_state_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Description', models.TextField(blank=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='Product_Images/')),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.category')),
                ('Farmer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.farmer_reg')),
            ],
        ),
    ]
