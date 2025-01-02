from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),  # Auth URLs for login, logout, password management
    path('members/', include('members.urls')),  # Custom URLs for the members app
    
    
]
