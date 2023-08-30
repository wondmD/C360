
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('resource.urls')),
    path('api/' , include('api.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
