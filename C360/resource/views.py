from django.shortcuts import render
from django.http import HttpResponse
from .models import course
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def resource(request):
    page_user = request.user
    if page_user.is_authenticated:
        page_user = page_user
    courses = course.objects.all()
    department = page_user.department
    context = {'page_user':page_user, 'courses':courses, 'department':department}
    messages.success(request, 'You have successfully authenticated as '+ request.user.username)
    return render(request, 'resource/resources.html', context)
