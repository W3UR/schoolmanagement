from django import forms
from .models import CustomUser, Module
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'role', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'mobile', 'profile_picture']

class ModuleAccessForm(forms.ModelForm):
    allowed_modules = forms.ModelMultipleChoiceField(
        queryset=Module.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = CustomUser
        fields = ['allowed_modules']

class UserRoleUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role']
