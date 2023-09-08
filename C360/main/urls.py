from django.urls import path
from . import views
urlpatterns =[
    path ("", views.index, name='home'),
    path('login/', views.login_page,  name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logoutuser, name='logout')
]