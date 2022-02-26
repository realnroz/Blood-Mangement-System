
from django import forms
from django.forms import ModelForm
from . models import BloodDonor


class DonorProfileForm(ModelForm):
    class Meta:
        model = BloodDonor
        fields = ('first_name','last_name','gender','dob','city','blood_group','mobile_number','profile_image')
        widgets={
            'first_name':forms.TextInput(attrs={'required':'True'}),
            'last_name':forms.TextInput(attrs={'required':'True'}),
            'gender':forms.Select(attrs={'required':'True'}),
            'dob':forms.DateInput(attrs={'required':'True','type':'date'}),
            'city':forms.TextInput(attrs={'required':'True'}),
            'blood_group':forms.Select(attrs={'required':'True'}),
            'mobile_number':forms.NumberInput(attrs={'required':'True'}),
        }
        labels={
            'city':'Where do you live ?',
            'blood_group':"What is your Blood-Group ?",
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
         model = BloodDonor
         fields = ['first_name','last_name','gender','dob','city','blood_group','mobile_number','profile_image']

class StatusUpdateForm(forms.ModelForm):
    class Meta:
         model = BloodDonor
         fields = ['is_available']

         labels={
            'is_available':'Are you available for the blood donation at the moment?'
         }