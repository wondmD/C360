from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from resource.models import course
from django.contrib.auth.decorators import login_required
from .forms import GroupForm
from curriculum.models import semister

# Create your views here.
@login_required(login_url='login')
def group_page(request, group_id):
    page_user= request.user
    messages = Message.objects.all()
    this_group = group.objects.get(id=group_id)
    courses = course.objects.all()
    semisters = semister.objects.all()
    this_group.participants.add(request.user)

    if (request.user.is_authenticated):
        page_user = request.user
    if request.method == 'POST':
        
        message = Message.objects.create(
            user=request.user,
            room=this_group,
            body=request.POST.get('body'),
            attachment = request.FILES.get('attachment')
            
        )
        
        
        return redirect('group_page', group_id=this_group.id)
    context = {'page_user':page_user,'group':this_group, 'messages':messages,'courses':courses, 'page_user':page_user, 'semisters':semisters}
    return render(request , 'groupapp/group.html',context)

def deleteMessage(request, message_id):
    message = Message.objects.get(id=message_id)

    if request.user != message.user:
        return HttpResponse('Your are not allowed here!!')

    if request.method == 'POST':
        message.delete()
        
        
        return redirect('resource')
    return render(request, 'groupapp/delete.html', {'obj': message})

@login_required(login_url='login')
def create_group(request, course_id):
    form = GroupForm()
    topic = course.objects.get(id=course_id)
    page_user = request.user
    if request.method == 'POST':
        group.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        ) 
        return redirect('resource')

    context = {'page_user':page_user,'form': form, 'topic': topic}
    return render(request, 'groupapp/create_group.html', context)

@login_required(login_url='login')
def all_group(request):
    page_user = request.user
    groups = group.objects.all()
    context = {'groups':groups, 'page_user':page_user}
    return render(request, 'groupapp/all_group.html', context)
