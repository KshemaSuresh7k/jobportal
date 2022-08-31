from django import forms
from.models import jobseeker
from.models import employee

class AddForm(forms.ModelForm):
    class Meta:
        model=jobseeker

        fields=('name','address','age','qualification','email','phonenumber','applyfor','workingmode','username','password')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'qualification':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'applyfor':forms.TextInput(attrs={'class':'form-control'}),
            'workingmode':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

class AddForm1(forms.ModelForm):
    class Meta:
        model=employee

        fields=('name','address','age','email','phonenumber','username','password')

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }
