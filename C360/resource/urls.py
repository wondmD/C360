from django.urls import path
from . import views
urlpatterns =[
    path('resource', views.resource, name="resource"),
    path('like/<int:course_id>/', views.increase_rating, name='increase_rating'),
    path('course/<int:course_id>/', views.course_detail, name="course_detail"),
    path('search/', views.search_course, name='search'),
]
