from django import forms
from .models import Route, Stoppage, TransportAssignment
from students.models import Student

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
        }

class StoppageForm(forms.ModelForm):
    class Meta:
        model = Stoppage
        fields = ['route', 'name']
        widgets = {
            'route': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'name': forms.TextInput(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
        }

class TransportAssignmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100 student-search', 'style': 'color: black;'})
    )

    class Meta:
        model = TransportAssignment
        fields = ['student', 'route', 'stoppage']
        widgets = {
            'route': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
            'stoppage': forms.Select(attrs={'class': 'border rounded p-2 w-full bg-gray-100', 'style': 'color: black;'}),
        }
