from django.shortcuts import render
from django.http import HttpResponse
from .models import course
# Create your views here.
def resource(request):
    courses = course.objects.all()
    return render(request, 'resource/resources.html', {'courses':courses})
