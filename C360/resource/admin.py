from django.contrib import admin
from .models import *
# Register your models here.
 
admin.site.register(resource)
admin.site.register(course)
admin.site.register(CourseLike)