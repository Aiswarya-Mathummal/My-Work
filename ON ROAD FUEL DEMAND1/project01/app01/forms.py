from django import forms
from .models import customer, fuel_details, Petrol_bunk, city, fuel_request


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}), )

    class Meta():
        model = customer
        fields = ('Name', 'phone_no', 'email', 'password')


class bunkForm(forms.ModelForm):
    class Meta():
        model = Petrol_bunk
        fields = ('name', 'image', 'email', 'password')


class user_regForm(forms.ModelForm):
    class Meta():
        model = customer
        fields = ('Name', 'phone_no', 'email', 'password', 'city', 'district', 'state')


class loginForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('email', 'password')


class editForm(forms.ModelForm):
    class Meta():
        model = customer
        fields = ('Name', 'phone_no', 'email', 'password', 'state', 'district', 'city')
        # exclude = ['user_id', 'email', 'password']


class deleteForm(forms.ModelForm):
    class Meta():
        model = customer
        fields = ('Name', 'phone_no', 'email')


class fuel_detForm(forms.ModelForm):
    class Meta():
        model = fuel_details
        fields = ('fuel_type', 'Rate')


class cityForm(forms.ModelForm):
    class Meta:
        model = city
        fields = ['city']

class Edituserform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, }))
    class Meta():
        model = customer
        fields = ('Name','address','phone_no','state','city','password')

class Editadminprofileform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= customer
        fields=('Name','address','phone_no','state','city','password',)


class fuelreqform(forms.ModelForm):
    CHOICES = [
        ('1', '1Ltr'),
        ('2', '2Ltr'),
        ('3', '3Ltr'),
        ('4', '4Ltr'),
        ('5', '5Ltr'),
    ]
    quantity = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    class Meta():
        model = fuel_request
        fields = ('fuel_type', 'quantity','price')