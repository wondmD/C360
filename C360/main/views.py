from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .models import myusers
from .backends import MyUserBackend
from django.contrib.auth.hashers import make_password
# Create your views here.
def index(request):
    page_user = request.user
    if page_user.is_authenticated:
        context = {'page_user':page_user}
        return render(request, "home.html", context)
    else:
        return render(request,"home.html")

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')
        authbackend = MyUserBackend()
        user = authbackend.authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('resource')
            
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'main/login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'main/register.html', context)

def about(request):
    return render(request, 'about.html')