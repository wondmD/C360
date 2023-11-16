from django.urls import path
from . import views
urlpatterns =[
    path ("", views.index, name='home'),
    path('login/', views.login_page,  name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('about/', views.about, name="about"),
    path('addsuperu/', views.register_superuser, name='register_superuser'),
    path('userx/<id>/', views.user_profile, name='user_profile'),
    path('editme/<user_id>/', views.edit_user, name='edit_user'),
    path('emailerror/', views.email_error, name='email_error')
]