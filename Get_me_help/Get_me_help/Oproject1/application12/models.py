from django.db import models

# Create your models here.

class register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    usertype = models.IntegerField(default=2)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return str(self.reg_id)
class service_center(models.Model):
    center_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phoneNo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    id = models.ImageField(upload_to='service_center_id/', null=True, blank=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    usertype = models.IntegerField(default=3)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.center_id)

class service_request(models.Model):
    req_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=500)
    image= models.ImageField(upload_to='image/', null=True, blank=True)
    vehicle_type = models.CharField(max_length=100)
    reg_id=models.ForeignKey('register', on_delete=models.CASCADE,to_field='reg_id')
    center_id=models.ForeignKey('service_center', on_delete=models.CASCADE,to_field='center_id')
    requested_on=models.DateField(auto_now_add=True)
    req_status = models.BooleanField(default=True)
    service_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.req_id)

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


class service_center_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude= models.DecimalField(max_digits=9, decimal_places=6)
    longitude= models.DecimalField(max_digits=9, decimal_places=6)
    center_id=models.ForeignKey('service_center', on_delete=models.CASCADE,to_field='center_id')

    def __str__(self):
        return str(self.location_id)


class chatroom(models.Model):
    chat_id = models.AutoField(primary_key=True)
    req_id=models.ForeignKey('service_request',on_delete=models.CASCADE,to_field='req_id')
    chat_key=models.CharField(max_length=200)
    chat_status = models.BooleanField(default=True)


class Message(models.Model):
    msg_id = models.AutoField(primary_key=True)
    chatkey=models.CharField(max_length=200)
    room = models.ForeignKey(chatroom, on_delete=models.CASCADE,to_field='chat_id')
    content = models.TextField()
    from_id=models.IntegerField()
    to_id=models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)