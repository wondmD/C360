from django import forms
from .models import myusers

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = myusers
        fields = ['username', 'email', 'password','department','semister']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = myusers
        fields = ['username', 'email','department','profile_pic','semister']