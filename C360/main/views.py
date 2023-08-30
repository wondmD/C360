from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, "home.html")

def login_page(request):
    return render(request, 'main/login.html')

def register_page(request):
    form = UserCreationForm
    context = {'form':form}
    return render(request, 'main/register.html', context)