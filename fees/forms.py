from django import forms
from .models import FeesGroup, FeesType

class FeesGroupForm(forms.ModelForm):
    class Meta:
        model = FeesGroup
        fields = ['name', 'amount_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Class name / Tran Stop'}),
            'amount_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'One Time / Monthly'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalnum():
            raise forms.ValidationError("Special characters not allowed!")
        return name

class FeesTypeForm(forms.ModelForm):
    class Meta:
        model = FeesType
        fields = ['fee_group', 'name', 'amount']
        widgets = {
            'fee_group': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Admis. Fee / Apr25'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '5100'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.replace(" ", "").isalnum():
            raise forms.ValidationError("Special characters not allowed!")
        return name
