from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import course
from curriculum.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from groupapp.models import group

# Create your views here.

@login_required(login_url='login')
def resource(request):
    page_user = request.user
    if page_user.is_authenticated:
        page_user = page_user
    courses = course.objects.all()
    semisters= semister.objects.all()
    groups = group.objects.all()
    department = page_user.department
    
    context = {'page_user':page_user, 
        'courses':courses, 
        'department':department, 
        'semisters':semisters,
        'groups':groups}

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

def search_course(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            course_obj = course.objects.filter(name__icontains=query)
        else:
            course_obj = None
        context = {'course_obj': course_obj, 'query': query}
        return render(request, 'resource/search.html', context)
    else:
        return render(request, 'resource/search.html')
