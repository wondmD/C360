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
from django.core.files.storage import FileSystemStorage
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
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()

            # Save the profile picture separately
            profile_pic = request.FILES.get('profile_pic')
            if profile_pic:
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                user.profile_pic = filename
                user.save()

            return redirect('login')

    context = {'form': form}
    return render(request, 'main/register.html', context)

def about(request):
    return render(request, 'about.html')

def register_superuser(request):
    if request.method == 'POST':
        passcode = request.POST.get('code')
        form = CreateUserForm(request.POST)
        if form.is_valid() and passcode=='wond1234':
            user = form.save(commit=False)
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('admin:index')  # Redirect to Django admin index page
    else:
        form = CreateUserForm()
    return render(request, 'main/register_superuser.html', {'form': form})

