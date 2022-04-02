"""animalDetectionSystem URL Configuration

   
"""

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userManagementSystem/',include('django.contrib.auth.urls')),
    path('userManagementSystem/',include('userManagementSystem.urls')),
]
