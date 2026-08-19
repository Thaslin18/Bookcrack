from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone_number', 'street_name', 'town_city', 'district', 'state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'street_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street name / House No'}),
            'town_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town or City'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'District'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }