from django import forms
from .models import Customer,Architect,Interior_Designer,Exterior_Designer,Plan,Exterior_Design,Interior_Design



class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = Customer
        fields= ('customer_id','customer_name','address','district','email','phone_no','password')

class ArchitectForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = Architect
        fields = ('architect_id','architect_name','address','district','email','phone_no','photo','password')

class InteriorDesignerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = Interior_Designer
        fields = ('interior_designer_id','name','address','district','email','phone_no','photo','password')

class ExteriorDesignerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = Exterior_Designer
        fields = ('exterior_designer_id','name','address','district','email','phone_no','photo','password')

#loginForm

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = Customer
        fields = ('email','password')


        fields = ('email','password')

#edit customer profile and view

class Editcustomerform(forms.ModelForm):
    class Meta():
        model = Customer
        fields = ('customer_name','address','district','phone_no')

class Editarchitectform(forms.ModelForm):
    class Meta():
        model = Architect
        fields = ('architect_name','photo','address','district','phone_no')

class Editinteriordesignerform(forms.ModelForm):
    class Meta():
        model = Interior_Designer
        fields = ('name','photo','address','district','phone_no')

class Editexteriordesignerform(forms.ModelForm):
    class Meta():
        model = Exterior_Designer
        fields = ('name','photo','address','district','phone_no')

#plans--------------------------------------------------------------------------------------------

class Addplanform(forms.ModelForm):
    class Meta():
        model = Plan
        fields = ('plan_name','sqft','floor','plan_image','blueprint','budget')

class Editplanform(forms.ModelForm):
    class Meta():
        model = Plan
        fields = ('plan_name','sqft','floor','plan_image','blueprint','budget')



#exterior design-------------------------------------------------------------------------------------------------

class Addexteriordesignform(forms.ModelForm):
    class Meta():
        model = Exterior_Design
        fields = ('details','budget','exterior_design_image')

class Editexteriordesignform(forms.ModelForm):
    class Meta():
        model = Exterior_Design
        fields = ('details','budget','exterior_design_image')

#Interior design------------------------------------------------------------------------------------------


class Addinteriordesignform(forms.ModelForm):
    class Meta():
        model = Interior_Design
        fields = ('details', 'budget','interior_design_image')


class Editinteriordesignform(forms.ModelForm):
    class Meta():
        model = Interior_Design
        fields = ('details', 'budget','interior_design_image')