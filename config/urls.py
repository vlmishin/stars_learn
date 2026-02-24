from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('courses.urls')),
    path('', include('courses.urls')),
    path('materials/', include('materials.urls')),
    path('', include('materials.urls')),
]
