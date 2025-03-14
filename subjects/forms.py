from django import forms
from .models import Class, Section, Subject, SubjectAssignment

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'section', 'room_number']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class SubjectAssignmentForm(forms.ModelForm):
    class Meta:
        model = SubjectAssignment
        fields = ['class_name', 'subject', 'teacher']
