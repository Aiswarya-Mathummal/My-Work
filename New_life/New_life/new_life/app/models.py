from django.db import models

# Create your models here.

class user_reg(models.Model):
    reg_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    usertype=models.IntegerField(default=2)
    password=models.CharField(max_length=100)

    def __str__(self):
        return str(self.reg_id)

class ambulance_drivers(models.Model):
    driver_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    phone_no = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    id=models.ImageField(upload_to='driver_id/',null=True,blank=True)
    profile_pic=models.ImageField(upload_to='driver_pic/',null=True,blank=True)
    usertype=models.IntegerField(default=3)
    status=models.BooleanField(default=False)
    available = models.BooleanField(default=True)


    def __str__(self):
        return str(self.driver_id)

class hospital(models.Model):
    hospital_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    phone_no = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    image=models.ImageField(upload_to='hospitals/',null=True,blank=True)
    id=models.ImageField(upload_to='hospital_certificate/',null=True,blank=True)
    usertype=models.IntegerField(default=4)
    status=models.BooleanField(default=False)


    def __str__(self):
        return str(self.hospital_id)

class ambulance(models.Model):
    ambulance_id=models.AutoField(primary_key=True)
    owner_id = models.ForeignKey('ambulance_drivers', on_delete=models.CASCADE,to_field='driver_id')
    vehicle_no = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    vehicle_status=models.BooleanField(default=True)
    image=models.ImageField(upload_to='ambulance/',null=True,blank=True)

    def __str__(self):
        return str(self.ambulance_id)

class patient_details(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    reason=models.TextField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    latitude= models.DecimalField(max_digits=9, decimal_places=6)
    longitude= models.DecimalField(max_digits=9, decimal_places=6)
    requestor_id=models.ForeignKey('user_reg', on_delete=models.CASCADE,to_field='reg_id')
    hospital=models.ForeignKey('hospital', on_delete=models.CASCADE,to_field='hospital_id')

    def __str__(self):
        return str(self.patient_id)

class booking_details(models.Model):
    booking_id=models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('patient_details', on_delete=models.CASCADE,to_field='patient_id')
    booked_on=models.DateTimeField(auto_now_add=True)
    driver_id=models.ForeignKey('ambulance_drivers', on_delete=models.CASCADE,to_field='driver_id')
    driver_status=models.CharField(max_length=100,default="Driver Assigned",choices={('Ride Started','Ride Started'),('Picked Patient','Picked Patient'),('Ride In Progress','Ride In Progress'),('Ride Completed','Ride Completed')})
    booking_status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.booking_id)



class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state=models.CharField(max_length=100)

    def __str__(self):
        return str(self.state_id)

class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city=models.CharField(max_length=100)
    state_id=models.IntegerField(default=1)

    def __str__(self):
        return str(self.city_id)

class complaints(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint=models.TextField(blank=False)
    complaint_status=models.BooleanField(default=True)
    reply=models.TextField(default="",blank=True)
    reply_status=models.BooleanField(default=True)
    booking_id=models.ForeignKey('booking_details', on_delete=models.CASCADE,to_field='booking_id')

    def __str__(self):
        return str(self.complaint_id)

class rate(models.Model):
    rate_id = models.AutoField(primary_key=True)
    rate_count=models.IntegerField(default=0)
    booking_id=models.ForeignKey('booking_details', on_delete=models.CASCADE,to_field='booking_id')

    def __str__(self):
        return str(self.rate_id)

class driver_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    latitude= models.DecimalField(max_digits=9, decimal_places=6)
    longitude= models.DecimalField(max_digits=9, decimal_places=6)
    driver_id=models.ForeignKey('ambulance_drivers', on_delete=models.CASCADE,to_field='driver_id')

    def __str__(self):
        return str(self.location_id)