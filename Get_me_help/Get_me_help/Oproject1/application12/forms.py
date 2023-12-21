from django import forms
from .models import register, service_center, service_request


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=5)
    class Meta():
         address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
         model = register
         fields = ('name','email','password','phoneNo','address','profile_pic',)

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=8)
    class Meta():
          model = register
          fields = ('email','password')

class service_center_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=8)
    class Meta():
        address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
        model = service_center
        fields = ('name','email','password','phoneNo','address','profile_pic','id')

class EditCustomerForm(forms.ModelForm):
    class Meta():
        model = register
        fields = ('name','password','phoneNo','address','profile_pic','state','city')

class EditService_Center_Form(forms.ModelForm):
    class Meta():
        model = service_center
        fields = ('name','address','phoneNo','password','state','city','profile_pic')

class EditUserForm(forms.ModelForm):
    class Meta():
        model = register
        fields = ('name','password','phoneNo','address','profile_pic','state','city')

class Request_form(forms.ModelForm):
    class Meta():
        complaint = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
        model = service_request
        fields = ('complaint','image','vehicle_type')

