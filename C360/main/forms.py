from django import forms
from .models import myusers
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = myusers
        fields = ['username', 'email', 'password']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = myusers
        fields = ['username', 'email','department','profile_pic','semister']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))
        self.helper.layout = Layout(
            'username',
            'email',
            'password',
            'department',
            'semester',
        )