from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from curriculum.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from groupapp.models import group
from django.shortcuts import redirect, get_object_or_404
from .forms import CourseForm, ResourceForm
from groupapp.forms import GroupForm


   


@login_required(login_url='login')
def like_course(request, course_id):
    try:
        if request.method == 'POST':
            course_t = get_object_or_404(course, id=course_id)
            if CourseLike.objects.filter(course=course_t, user=request.user).exists():
                to_be_deleted = CourseLike.objects.filter(course=course_t, user=request.user)
                to_be_deleted.delete()
                # CourseLike already exists for this user and course
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                CourseLike.objects.create(course=course_t, user=request.user)
                return redirect(request.META.get('HTTP_REFERER'))
    except IntegrityError:
        return redirect('resource')

    
@login_required(login_url='login')
def resource_view(request):
    page_user = request.user
    if page_user.is_authenticated:
        page_user = page_user
    courses = course.objects.all()
    semisters= semister.objects.all()
    groups = group.objects.all()
    department = page_user.department   
    likes= CourseLike.objects.all()
    context = {'page_user':page_user, 
        'courses':courses, 
        'department':department, 
        'semisters':semisters,
        'groups':groups,
        'likes':likes}

    return render(request, 'resource/index.html', context)



 
@login_required(login_url='login')
def course_detail(request, course_id):
    page_user = request.user
    resources= resource.objects.all()
    cource = course.objects.get(id=course_id)
    semisters = semister.objects.all()
    context = {'target_course':cource, 'page_user':page_user, 'resources':resources, 'semisters':semisters}

    return render(request, 'resource/course.html', context)
@login_required(login_url='login')
def search_course(request):
    page_user = request.user
    semisters = semister.objects.all()
    groups =group.objects.all()
    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            course_obj = course.objects.filter(name__icontains=query)
        else:
            course_obj = None
        context = {'course_obj': course_obj, 'query': query, 'page_user':page_user, 'groups':groups, 'semisters':semisters}
        return render(request, 'resource/search.html', context)
    else:
        return render(request, 'resource/search.html')
    

@login_required(login_url='login') 
def find_by_sem(request, id):
    groups = group.objects.all()
    courses = course.objects.all()
    semisters= semister.objects.all()
    page_user = request.user
    t_semister = semister.objects.get(id=id)
    context = {'groups':groups,'page_user':page_user,'t_semister':t_semister, 'semisters':semisters, 'courses':courses}
    return render(request, 'resource/find_by_sem.html', context)

@login_required(login_url='login')
def add_edit_course(request, course_id=None):
    page_user = request.user

    # If course_id is provided, fetch the existing course instance, otherwise create a new one
    if course_id:
        instance = course.objects.get(id=course_id)
    else:
        instance = None
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if instance == None:
                form = GroupForm()
                topic = course.objects.get(id=course_id)
                group.objects.create(
                    host=request.user,
                    topic=topic,
                    name=request.POST.get('name'),
                    ) 
            return redirect('resource')  # Replace 'course_list' with the actual URL name for the course list view
    else:
        form = CourseForm(instance=instance)
    
    context = {
        'form': form,
        'page_user':page_user
    }
    return render(request, 'resource/add_edit_course.html', context)

def myadmin(request):
    page_user = request.user
    context = {'page_user':page_user}
    return render(request, 'resource/admin.html', context)

@login_required(login_url='login')
def all_course(request):
    courses = course.objects.all()
    page_user = request.user
    semisters = semister.objects.all()
    groups = group.objects.all()
    context = {
        'courses': courses,
        'page_user':page_user,
        'semisters': semisters,
        'groups': groups}
    return render(request, 'resource/allcourse.html', context)

def propage(request):
    return render(request, 'resource/c360pro.html')


@login_required(login_url='login')
def add_edit_resource(request, resource_id=None, course_id=None):
    course = course.objects.get(id=course_id)
    page_user = request.user
    if resource_id:
        instance = resource.objects.get(id=resource_id)
    else:
        instance = None
    if request.method == 'POST':       
        form = ResourceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            # Assuming your Resource model has a foreign key to Course
            resource = form.save(commit=False)
            resource.course = course
            resource.save()
            return redirect('resource')
    else:
        form = ResourceForm(instance=instance)
    
    context = {
        'form': form,
        'page_user':page_user
    }
    return render(request, 'resource/add_edit_resource.html', context)