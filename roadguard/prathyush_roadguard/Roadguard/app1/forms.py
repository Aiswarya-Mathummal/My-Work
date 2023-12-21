from django import forms
from .models import register, Officers, traffic_rule_violation, vehicle_details, offences


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),

    class Meta():
        model = register
        fields = ('first_name','last_name','address','phone_no','email','password','id',)


class loginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)

    class Meta():
        model = register
        fields = ('email','password')


class EdituserForm(forms.ModelForm):
    class Meta():
        model = register
        fields = ('first_name','last_name','address','phone_no','state','city','password')



class addOfficerForm(forms.ModelForm):
    class Meta():
        model = Officers
        fields = ('name','phone_no','station','email','id_proof',)

class EditOfficerForm(forms.ModelForm):
    class Meta():
        model = Officers
        fields = ('password','name','phone_no','station','state','city',)

class Editadminprofileform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= register
        fields=('first_name','last_name','address','phone_no','password',)


class addvehicledetailsform(forms.ModelForm):
    class Meta():
         model= vehicle_details
         fields=('vehicle_no','images',)

class editvehicledetailsform(forms.ModelForm):
    class Meta():
         model= vehicle_details
         fields=('images',)

class Addviolationform(forms.ModelForm):
    details=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= traffic_rule_violation
         fields=('violation','details','fine')


class editviolationform(forms.ModelForm):
    details=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= traffic_rule_violation
         fields=('violation','details','fine')


class reportoffenceform(forms.ModelForm):
    details=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= offences
         fields=('violation_id','vehicle_no','details','image')


class editoffenceform(forms.ModelForm):
    details=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= offences
         fields=('violation_id','vehicle_no','details','image')