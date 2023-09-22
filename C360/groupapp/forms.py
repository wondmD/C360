from django.forms import ModelForm
from .models import group

class GroupForm(ModelForm):
    class Meta:
        model = group
        fields = '__all__'
        exclude = ['host', 'participants','topic']