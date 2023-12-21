from django import forms
from .models import customers,recycling_unit,product,category
class recyclingform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),

    class Meta():
        model = recycling_unit
        fields = ('unit_name','phone','address','state','district','city','email','password','profile_pic','id_proof')




class registerform(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter user name '}))
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    forms.Textarea(attrs={'rows': 2, 'cols': 15}),
    class Meta():
         model= customers
         fields=('reg_id','user_name','firstname','lastname','phone','address','state','district','city','email','password','profile_pic','id_proof',)

class Editcustomerform(forms.ModelForm):
    class Meta():
        address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}))
        model=customers
        fields=('firstname','lastname','address','state','district','city','password','profile_pic',)


class Loginform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=12, min_length=5)
    class Meta():
        model = customers
        fields = ('email','password')


class Editrecyclingform(forms.ModelForm):
    class Meta():

        password = forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=5)
        address=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
        forms.Textarea(attrs={'rows': 2, 'cols': 15}),


        model = recycling_unit
        fields = ('unit_name','phone','address','state','district','city','password','profile_pic',)
class addCategoryForm(forms.ModelForm):
    class Meta():
        model = category
        fields = ('category_name',)


class editCategoryForm(forms.ModelForm):
    class Meta():
        model = category
        fields = ('category_name',)

#
class Addproductsform(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= product
         fields=('categories','name','description','price','image')

class editproductsform(forms.ModelForm):
    description=forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
    class Meta():
         model= product
         fields=('categories','name','description','price','image')