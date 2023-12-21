from django.db import models

# Create your models here.

class register(models.Model):
    reg_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    usertype=models.IntegerField(default=2)
    password=models.CharField(max_length=100)

    def __str__(self):
        return str(self.reg_id)

class tailor(models.Model):
    tailor_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    phone_no = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='tailor_pic/',null=True,blank=True)
    id=models.ImageField(upload_to='tailor_id/',null=True,blank=True)
    usertype=models.IntegerField(default=3)
    status=models.BooleanField(default=False)


    def __str__(self):
        return str(self.tailor_id)

class manufacturer(models.Model):
    manufacturer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    phone_no = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='manufacturer_pic/',null=True,blank=True)
    id=models.ImageField(upload_to='manufacturer_id/',null=True,blank=True)
    usertype=models.IntegerField(default=4)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.manufacturer_id)

class designer(models.Model):
    designer_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.TextField(blank=True)
    phone_no = models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='designer_pic/',null=True,blank=True)
    id=models.ImageField(upload_to='designer_id/',null=True,blank=True)
    usertype=models.IntegerField(default=5)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.designer_id)

class delivery_agent(models.Model):
    agent_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='agent_pic/',null=True,blank=True)
    id_proof=models.ImageField(upload_to='agent_id/', blank=True, null=True)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.IntegerField(default=6)
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.agent_id)


class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class designs(models.Model):
    design_id=models.AutoField(primary_key=True)
    categories=models.ForeignKey('category',on_delete=models.CASCADE,to_field='category_id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='design_images/', blank=True, null=True)
    designer_id=models.ForeignKey('designer',on_delete=models.CASCADE,to_field='designer_id')

    def __str__(self):
        return str(self.design_id)


class materials(models.Model):
    material_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='design_images/', blank=True, null=True)
    manufacturer_id=models.ForeignKey('manufacturer',on_delete=models.CASCADE,to_field='manufacturer_id')


    def __str__(self):
        return str(self.material_id)


class sewing_request(models.Model):
    req_id = models.AutoField(primary_key=True)
    design_id = models.ForeignKey('designs', on_delete=models.CASCADE, to_field='design_id')
    material_id1 = models.IntegerField()
    material_id2 = models.IntegerField(blank=True,null=True)
    material_id3 = models.IntegerField(blank=True,null=True)
    user_id = models.ForeignKey('register', on_delete=models.CASCADE, to_field='reg_id')
    tailor_id = models.ForeignKey('tailor', on_delete=models.CASCADE, to_field='tailor_id')
    requested_on=models.DateField(auto_now_add=True)
    delivery_date=models.DateField(auto_now_add=False,blank=True,null=True)
    measurement_status = models.BooleanField(default=False)
    request_status=models.BooleanField(default=False)
    rate_given = models.BooleanField(default=False)


    def __str__(self):
        return str(self.req_id)

class sewing_details(models.Model):
    sewing_id=models.AutoField(primary_key=True)
    request_id=models.ForeignKey('sewing_request',on_delete=models.CASCADE,to_field='req_id')
    measurement_id=models.ForeignKey('sewing_measurements',on_delete=models.CASCADE,to_field='measurement_id')
    fabric1_qty=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    fabric2_qty=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True,default=0)
    fabric3_qty=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True,default=0)
    price1 = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    price2 = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    price3 = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    sewing_charge= models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    design_charge= models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)

    tailor_status = models.CharField(max_length=100,default="Waiting For your Response")
    sewing_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sewing_id)

class sewing_measurements(models.Model):
    measurement_id=models.AutoField(primary_key=True)
    brand_size=models.CharField(max_length=100)
    chest_measurement=models.DecimalField(max_digits=10, decimal_places=2)
    waist_measurement=models.DecimalField(max_digits=10, decimal_places=2)
    hip_measurement=models.DecimalField(max_digits=10, decimal_places=2)
    shoulder_measurement=models.DecimalField(max_digits=10, decimal_places=2)
    sleeve_length=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    outseam_length=models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    request_id=models.ForeignKey('sewing_request',on_delete=models.CASCADE,to_field='req_id')


    def __str__(self):
        return str(self.measurement_id)

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    sewing_id=models.ForeignKey('sewing_details',on_delete=models.CASCADE,to_field='sewing_id')
    order_date=models.DateField(auto_now_add=False,blank=True,null=True)
    deliver_status= models.CharField(max_length=100,default="The delivery agent is still unassigned.")
    tailor_status = models.CharField(max_length=100,default="Requested Manufactures For Fabrics")
    order_status = models.BooleanField(default=True)
    delivery_agent_status = models.BooleanField(default=False)
    material_req_status = models.BooleanField(default=False)
    pickup_date = models.DateField(auto_now_add=False,blank=True,null=True)
    pickup_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)

class material_request(models.Model):
    req_id=models.AutoField(primary_key=True)
    order_id = models.ForeignKey('orders', on_delete=models.CASCADE, to_field='order_id')
    material_id=models.ForeignKey('materials',on_delete=models.CASCADE,to_field='material_id')
    manufacturer_id=models.ForeignKey('manufacturer',on_delete=models.CASCADE,to_field='manufacturer_id')
    requested_on=models.DateField(auto_now_add=True)
    request_status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.req_id)

class assign_delivery_agent(models.Model):
    assign_id=models.AutoField(primary_key=True)
    order_id = models.ForeignKey('orders', on_delete=models.CASCADE, to_field='order_id')
    pickup_date=models.DateField(auto_now_add=False)
    pickup_status=models.BooleanField(default=False)
    deliver_status=models.BooleanField(default=False)
    agent_id=models.ForeignKey('delivery_agent',on_delete=models.CASCADE,to_field='agent_id')


    def __str__(self):
        return str(self.assign_id)