from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cv/', include('resume.urls')),
    path('production/', include('production.urls', namespace='production')),
    path('', home),
    
            ]
