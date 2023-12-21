from django.db import models

class register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)
    User_type=models.IntegerField(default=2)
    status=models.BooleanField(default=False)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    id = models.ImageField(upload_to='user_id/', blank=True, null=True)

    def __str__(self):
        return str(self.reg_id)



class Officers(models.Model):
    officer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    station = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    id_proof = models.ImageField(upload_to='officer_id/', blank=True, null=True)
    User_type = models.IntegerField(default=3)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=128)

    def __str__(self):
        return str(self.officer_id)

class state(models.Model):
    state_id =models.AutoField(primary_key=True)
    state=models.CharField(max_length=100)

    def __str__(self):
        return str(self.state_id)


class city(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    state_id = models.IntegerField(default=1)


    def __str__(self):
        return str(self.city_id)


class vehicle_details(models.Model):
    vehicle_id=models.AutoField(primary_key=True)
    owner_id = models.ForeignKey('register', on_delete=models.CASCADE, to_field='reg_id')
    vehicle_no = models.CharField(max_length=17, unique=True)  # Vehicle Identification Number
    images = models.ImageField(upload_to='vehicle_details/', null=True, blank=True)

    def __str__(self):
        return str(self.vehicle_id)

class traffic_rule_violation(models.Model):
    violation_id=models.AutoField(primary_key=True)
    violation = models.CharField(max_length=300)
    details = models.CharField(max_length=300)
    fine =  models.CharField(max_length=300)

    def __str__(self):
        return str(self.violation)

class offences(models.Model):
    offence_id=models.AutoField(primary_key=True)
    violation_id=models.ForeignKey('traffic_rule_violation', on_delete=models.CASCADE,to_field='violation_id')
    vehicle_no = models.CharField(max_length=300)
    details = models.CharField(max_length=300)
    image = models.ImageField(upload_to='offense_images/', blank=True, null=True)
    officer_id=models.ForeignKey('Officers', on_delete=models.CASCADE,to_field='officer_id')
    reporter_id = models.ForeignKey('register', on_delete=models.CASCADE, to_field='reg_id')
    reported_on=models.DateField(auto_now_add=True)
    offence_status = models.BooleanField(default=False)
    user_status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.offence_id)


class offenders(models.Model):
    offender_id=models.AutoField(primary_key=True)
    offence_id=models.ForeignKey('offences', on_delete=models.CASCADE,to_field='offence_id')
    user_id=models.ForeignKey('register', on_delete=models.CASCADE,to_field='reg_id',default=0)
    verified_on=models.DateField(auto_now_add=True)
    fine_paid_on=models.DateField(auto_now_add=False,blank=True,null=True)
    fine_status = models.BooleanField(default=False)
    offender_status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.offender_id)

