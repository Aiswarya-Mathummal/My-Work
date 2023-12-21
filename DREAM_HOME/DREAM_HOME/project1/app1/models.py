from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    user_type = models.IntegerField(default=2)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.customer_id)

class Architect(models.Model):
    architect_id = models.AutoField(primary_key=True)
    architect_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='architect_photo/', null=True, blank=True)
    user_type = models.IntegerField(default=3)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.architect_id)

class Interior_Designer(models.Model):
    interior_designer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='interior_designer_photo/', null=True, blank=True)
    user_type = models.IntegerField(default=4)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.interior_designer_id)


class Exterior_Designer(models.Model):
    exterior_designer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='exterior_designer_photo/', null=True, blank=True)
    user_type = models.IntegerField(default=5)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.exterior_designer_id)


class Plan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    architect_id = models.ForeignKey('Architect',on_delete=models.CASCADE,to_field='architect_id')
    plan_name = models.CharField(max_length=50)
    sqft = models.CharField(max_length=30)
    floor = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    budget = models.CharField(max_length=500)
    plan_image =models.ImageField(upload_to='plan_image/',null=True,blank=True)
    blueprint =models.ImageField(upload_to='blueprint/',null=True,blank=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.plan_id)

class Plan_Book(models.Model):
    plan_book_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer',on_delete=models.CASCADE,to_field='customer_id')
    architect_id = models.ForeignKey('Architect',on_delete=models.CASCADE,to_field='architect_id')
    plan_id = models.ForeignKey('Plan',on_delete=models.CASCADE,to_field='plan_id')
    status = models.BooleanField(default=False)
    requested_on=models.DateField(auto_now_add=True)
    book_date =models.DateField(auto_now_add=False,null=True,blank=True)


    def __str__(self):
        return str(self.plan_book_id)

class Exterior_Design(models.Model):
    exterior_design_id = models.AutoField(primary_key=True)
    exterior_designer_id = models.ForeignKey('Exterior_Designer',on_delete=models.CASCADE,to_field='exterior_designer_id')
    details = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    exterior_design_image = models.ImageField(upload_to='exterior_design_image/',null=True,blank=True)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.exterior_design_id)


class Interior_Design(models.Model):
    interior_design_id = models.AutoField(primary_key=True)
    interior_designer_id = models.ForeignKey('Interior_Designer',on_delete=models.CASCADE,to_field='interior_designer_id')
    details = models.CharField(max_length=100)
    budget = models.CharField(max_length=50)
    interior_design_image = models.ImageField(upload_to='interior_design_image/',null=True,blank=True)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.interior_design_id)


class EXT_design_book(models.Model):
    exterior_design_book_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, to_field='customer_id')
    exterior_designer_id = models.ForeignKey('Exterior_Designer',on_delete=models.CASCADE,to_field='exterior_designer_id')
    exterior_design_id = models.ForeignKey('Exterior_Design',on_delete=models.CASCADE,to_field='exterior_design_id')
    status = models.BooleanField(default=False)
    requested_on = models.DateField(auto_now_add=True)
    book_date = models.DateField(auto_now_add=False, null=True, blank=True)
    def __str__(self):
        return str(self.exterior_design_book_id)

class INT_design_book(models.Model):
    interior_design_book_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE, to_field='customer_id')
    interior_designer_id = models.ForeignKey('Interior_Designer',on_delete=models.CASCADE,to_field='interior_designer_id')
    interior_design_id = models.ForeignKey('Interior_Design',on_delete=models.CASCADE,to_field='interior_design_id')
    status = models.BooleanField(default=False)
    requested_on = models.DateField(auto_now_add=True)
    book_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return str(self.interior_design_book_id)
