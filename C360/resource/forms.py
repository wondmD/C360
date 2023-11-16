from django import forms
from .models import course, resource
from django.utils.safestring import mark_safe
class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter course name'})
        self.fields['semister'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': '3'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})
        self.fields['prerequest'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter prerequisite'})
        self.fields['crh'].widget.attrs.update({'class': 'form-control'})
        self.fields['course_type'].widget.attrs.update({'class': 'form-control'})

        # Add label classes and icons
        for field_name, field in self.fields.items():
            field.label = mark_safe(f'<strong><i class="fas fa-star"></i> {field.label}</strong>')

    class Meta:
        model = course
        fields = '__all__'
class ResourceForm(forms.ModelForm):
    field_icons = {
        'name': 'fas fa-file',
        'file': 'fas fa-upload',
        'description': 'fas fa-align-left',
    }

    class Meta:
        model = resource
        fields = ['name','file','description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter resource name'})
        self.fields['file'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': '3'})

        # Add label classes and icons
        for field_name, field in self.fields.items():
            icon_class = self.field_icons.get(field_name, '')
            if icon_class:
                field.label = mark_safe(f'<strong><i class="{icon_class}"></i> {field.label}</strong>')

    class Meta:
        model = resource
        fields = ['name','file','description']