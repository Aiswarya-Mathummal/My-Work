from django import forms
from . models import hospital,ambulance_drivers,user_reg,ambulance,patient_details,booking_details,complaints,rate
class userregisterform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),
    class Meta():
         model= user_reg
         fields=('firstname','lastname','address','phone_no','email','password',)

class Edituserform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= user_reg
        fields=('firstname','lastname','address','phone_no','state','city','password')


class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    class Meta():
        model = user_reg
        fields = ('email','password')

class ambulancedriverregform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),
    class Meta():
         model= ambulance_drivers
         fields=('firstname','lastname','address','phone_no','email','password','profile_pic','id')

class Editambulancedriverregform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= ambulance_drivers
        fields=('firstname','lastname','address','phone_no','state','city','password','profile_pic')



class hospitalregform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta():
         model= hospital
         fields=('name','address','phone_no','email','password','image','id')

class Edithospitalregform(forms.ModelForm):
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= hospital
         fields=('name','address','phone_no','state','city','image','password')


class Editadminprofileform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= user_reg
        fields=('firstname','lastname','address','phone_no','state','city','password',)


class Addambulanceform(forms.ModelForm):
    class Meta():
         model= ambulance
         fields=('vehicle_no','image',)

class editambulanceform(forms.ModelForm):
    class Meta():
         model= ambulance
         fields=('image',)

class Patientdetailsform(forms.ModelForm):
    CHOICES = [
        ('Male','Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)

    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
         model= patient_details
         fields=('name','age','gender','reason',)


class updateDriverstatusForm(forms.ModelForm):
    driver_status = forms.ChoiceField(
        choices=[('Ride Started', 'Ride Started'), ('Picked Patient', 'Picked Patient'),
                 ('Ride In Progress', 'Ride In Progress'), ('Ride Completed', 'Ride Completed')],
        widget=forms.RadioSelect(),
        required=True,
        initial='Ride Started',
        help_text='Choose your option',
        label='update status',
    )
    class Meta():
        model = booking_details
        fields=('driver_status',)

class createComplaintForm(forms.ModelForm):
    complaint = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, }))
    class Meta():
        model = complaints
        fields = ('complaint',)

class replyComplaintForm(forms.ModelForm):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, }))
    class Meta():
        model = complaints
        fields = ('reply',)

