from django import forms
from .models import myusers

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = myusers
        fields = ['username', 'email', 'password','department']