from django.urls import path
from . import views

urlpatterns = [
    path("resource2" , views.resource_page, name="resource2")
]
