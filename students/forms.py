from django import forms
from .models import Student
from django.core.exceptions import ValidationError
from subjects.models import Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'admission_number': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'first_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'last_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'father_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'mother_name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'mobile_number': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'email': forms.EmailInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),

            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'date_of_admission': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'student_class': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'gender': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'religion': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'caste_category': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'blood_group': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_class'].queryset = Class.objects.all()

    def clean_admission_number(self):
        admission_number = self.cleaned_data.get('admission_number')
        if Student.objects.filter(admission_number=admission_number).exists():
            raise ValidationError("Admission Number already exists.")
        return admission_number
