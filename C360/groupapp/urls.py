from django.urls import path
from .import views
urlpatterns = [
    path ('group/<int:group_id>/', views.group_page, name='group_page'),
    path ('create/<int:course_id>/', views.create_group, name='create_group' ),
    path ('allgroup/', views.all_group, name='all_group'),
    path ('delete/', views.deleteMessage, name='delete_m')
]