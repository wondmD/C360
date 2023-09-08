from django.shortcuts import render
from django.http import HttpResponse
from .models import course
# Create your views here.
def resource(request):
    page_user = request.user
    if page_user.is_authenticated:
        page_user = page_user
    courses = course.objects.all()
    department = page_user.department
    context = {'page_user':page_user, 'courses':courses, 'department':department}
    return render(request, 'resource/resources.html', context)
