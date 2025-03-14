from django import forms
from .models import SchoolProfile

class SchoolProfileForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-picker'}))

    class Meta:
        model = SchoolProfile
        fields = ['school_name', 'principal_name', 'address', 'email', 'mobile', 'registration_number', 'logo', 'start_date', 'end_date']
