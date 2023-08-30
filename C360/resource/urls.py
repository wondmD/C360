from django.urls import path
from . import views
urlpatterns =[
    path('resource', views.resource, name="resource")
]