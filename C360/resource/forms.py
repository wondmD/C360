from django import forms
from .models import course, resource

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'  
class ResourceForm(forms.ModelForm):

    class Meta:
        model = resource
        fields = '__all__'
        