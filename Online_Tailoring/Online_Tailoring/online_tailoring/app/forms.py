from django import forms
from .models import manufacturer, register, delivery_agent, designer, tailor, category, designs, materials, \
    sewing_measurements, orders


class registerform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),
    class Meta():
         model= register
         fields=('firstname','lastname','address','phone_no','state','district','city','email','password',)

class Editcustomerform(forms.ModelForm):
    class Meta():
        address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
        model= register
        fields=('firstname','lastname','address','phone_no','state','district','city','password')


class tailorregform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta():
         model= tailor
         fields=('firstname','lastname','address','phone_no','state','district','city','email','password','profile_pic','id')

class Edittailorregform(forms.ModelForm):
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= tailor
         fields=('profile_pic','firstname','lastname','address','phone_no','state','district','city','password',)

class manufacturerregform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta():
         model= manufacturer
         fields=('name','address','phone_no','state','district','city','email','password','profile_pic','id')

class Editmanufacturerregform(forms.ModelForm):
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= manufacturer
         fields=('profile_pic','name','address','phone_no','state','district','city','password',)


class designerregform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta():
        model = designer
        fields = ('firstname', 'lastname', 'address', 'phone_no', 'state', 'district', 'city', 'email', 'password', 'profile_pic',
        'id')


class Editdesignerregform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta():
        model = designer
        fields = ('profile_pic','firstname', 'lastname', 'address', 'phone_no', 'state', 'district', 'city', 'password', )


class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    class Meta():
        model = register
        fields = ('email','password')

class addDeliveryAgentForm(forms.ModelForm):
    class Meta():
        model = delivery_agent
        fields = ('name','email','profile_pic','id_proof')


class Editadminprofileform(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
    class Meta():
        model= register
        fields=('firstname','lastname','address','phone_no','state','city','password',)

class addCategoryForm(forms.ModelForm):
    class Meta():
        model = category
        fields = ('category_name',)


class editCategoryForm(forms.ModelForm):
    class Meta():
        model = category
        fields = ('category_name',)


class Adddesignform(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= designs
         fields=('categories','name','description','price','image')

class editdesignform(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= designs
         fields=('categories','name','description','price','image')

class Addmaterialform(forms.ModelForm):
    class Meta():
         model= materials
         fields=('name','price','image')

class editmaterialform(forms.ModelForm):
    class Meta():
         model= materials
         fields=('name','price','image')

class sewing_measurement_form(forms.ModelForm):
    CHOICES = [
        ('XS','XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('XXXXL', 'XXXXL'),
    ]
    brand_size =forms.ChoiceField(widget=forms.Select,choices=CHOICES)

    class Meta():
         model= sewing_measurements
         fields=('brand_size','chest_measurement','waist_measurement','hip_measurement','shoulder_measurement','sleeve_length','outseam_length',)


class update_tailor_status_form(forms.ModelForm):
    CHOICES = [
        ('Fabrics Collected','Fabrics Collected'),
        ('Sewing On Progress', 'Sewing On Progress'),
        ('Final finishing', 'Final finishing'),
        ('stitching finished', 'stitching finished'),
    ]
    tailor_status =forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)

    class Meta():
         model= orders
         fields=('tailor_status',)

