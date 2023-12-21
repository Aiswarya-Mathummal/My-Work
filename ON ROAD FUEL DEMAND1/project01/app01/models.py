from django.db import models
from django.contrib.auth.models import User


class customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    User_type = models.IntegerField(default=2)
    status = models.BooleanField(default=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_id)


class fuel_details(models.Model):
    fuel_id = models.AutoField(primary_key=True)
    fuel_type = models.CharField(max_length=100)
    Rate =models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return str(self.fuel_type)


class Petrol_bunk(models.Model):
    bunk_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    User_type = models.IntegerField(default=3)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bunk_id)


class fuel_request(models.Model):
    req_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    price=models.DecimalField(max_digits=9, decimal_places=6,default=0)
    fuel_type = models.ForeignKey('fuel_details', on_delete=models.CASCADE, to_field='fuel_id')
    userid = models.ForeignKey('customer', on_delete=models.CASCADE, to_field='user_id')
    bunkid = models.ForeignKey('Petrol_bunk', on_delete=models.CASCADE, to_field='bunk_id')
    req_status = models.BooleanField(default=False)

class bunk_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    bunk_id = models.ForeignKey('Petrol_bunk', on_delete=models.CASCADE, to_field='bunk_id')

    def __str__(self):
        return str(self.location_id)


class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=100)

    def __str__(self):
        return str(self.state_id)


class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    state_id = models.IntegerField(default=1)

    def __str__(self):
        return str(self.city_id)
