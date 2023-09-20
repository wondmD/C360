from django.shortcuts import render
from .models import *


# Create your views here.
def group_page(request):
    messages = Message.objects.all()
    groups = group.objects.all()
    context = {'groups':groups, 'messages':messages}
    return render(request , 'groupapp/group.html',context)