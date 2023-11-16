from django.urls import path
from . import views
urlpatterns =[
    path('resource/', views.resource_view, name="resource"),
    path('course/<int:course_id>/', views.course_detail, name="course_detail"),
    path('search/', views.search_course, name='search'),
    path('like/<int:course_id>', views.like_course, name='like_course'),
    path('bysem/<int:id>', views.find_by_sem, name='find_by_sem'),
    path('courseadd/', views.add_edit_course, name='add_course'),
    path('courseedit/<int:course_id>/', views.add_edit_course, name='edit_course'),
    path('myadmin/', views.myadmin, name='myadmin'),
    path('allcourse/', views.all_course, name='all_course'),
    path('pro/', views.propage, name='pro'),
    path('resourceadd/<int:course_id>', views.add_edit_resource, name='add_resource'),
    path('editresource/<int:resource_id>/', views.add_edit_resource, name='edit_resource')
]
