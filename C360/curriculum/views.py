from django.shortcuts import render
from .models import semister
# Create your views here.
def resource_page(request):
    semisters = semister.objects.all()
    return render(request, 'resource/resources.html', {'semisters':semisters})
