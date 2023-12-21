from django.db import models

# Create your models here.
class customers(models.Model):
    reg_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address =  models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)
    user_type = models.IntegerField(default=2)
    status = models.BooleanField(default=False)
    profile_pic= models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    id_proof= models.ImageField(upload_to='id_proof/',null=True,blank=True)

    def __str__(self):
        return str(self.reg_id)

class recycling_unit(models.Model):
    recycle_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=100)
    user_type = models.IntegerField(default=3)
    status = models.BooleanField(default=False)
    address =  models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)
    profile_pic= models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    id_proof= models.ImageField(upload_to='id_proof/',null=True,blank=True)

    def __str__(self):
        return str(self.recycle_id)


class product(models.Model):
    product_id=models.AutoField(primary_key=True)
    categories=models.ForeignKey('category',on_delete=models.CASCADE,to_field='category_id')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    expire_date=models.DateField(auto_now=False,blank=True,null=True)
    uploaded_on=models.DateField(auto_now=True)
    product_status=models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField( upload_to='product_i mages/', blank=True, null=True)
    customers_id=models.ForeignKey('customers',on_delete=models.CASCADE,to_field='reg_id')
    rating = models.IntegerField(default=0)
    rating_status=models.BooleanField(default=True)

    def __str__(self):
        return str(self.product_id)


class category(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

 # Replace with the actual import path for your Customers model

class product_request(models.Model):
    req_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('product', on_delete=models.CASCADE, to_field='product_id')
    buyer_id = models.ForeignKey('customers', on_delete=models.CASCADE, related_name='buyer', to_field='reg_id')
    seller_id = models.ForeignKey('customers', on_delete=models.CASCADE, related_name='seller', to_field='reg_id')
    requested_on = models.DateField(auto_now_add=True)
    req_status = models.BooleanField(default=True)
    approve_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.req_id)


class recycle_product(models.Model):
    rc_product_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('product', on_delete=models.CASCADE, to_field='product_id')
    uploaded_on = models.DateField(auto_now_add=True)
    product_status = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    rating_status=models.BooleanField(default=True)

    def __str__(self):
        return str(self.rc_product_id)

class recycle_product_request(models.Model):
    req_id = models.AutoField(primary_key=True)
    rc_product_id = models.ForeignKey('recycle_product', on_delete=models.CASCADE, to_field='rc_product_id')
    recycle_id = models.ForeignKey('recycling_unit', on_delete=models.CASCADE, related_name='seller', to_field='recycle_id')
    accepted_on = models.DateField(auto_now_add=True)
    accept_status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.req_id)


