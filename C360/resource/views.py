from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import course
from curriculum.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def resource(request):
    page_user = request.user
    if page_user.is_authenticated:
        page_user = page_user
    courses = course.objects.all()
    semisters= semister.objects.all()
    department = page_user.department
    context = {'page_user':page_user, 'courses':courses, 'department':department, 'semisters':semisters}
    messages.success(request, 'You have successfully authenticated as '+ request.user.username)
    return render(request, 'resource/resources.html', context)
@login_required(login_url='login')
def increase_rating(request, course_id):
    cource = course.objects.get(id=course_id)
    cource.increase_rating()
    return redirect('resource')  
@login_required(login_url='login')
def course_detail(request, course_id):
    cource = course.objects.get(id=course_id)
    context = {'target_course':cource}
    return render(request, 'resource/course.html', context)
