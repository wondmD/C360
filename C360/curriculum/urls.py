from django.urls import path
from . import views

urlpatterns = [
    path("" , views.resource_page, name="resource_page")
]
