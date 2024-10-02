# urls.py
from django.contrib import admin
from django.urls import path, include
from data_loader.admin import custom_admin_site  

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api_mock/', include('api_mock.urls')),
    path('custom-admin/', custom_admin_site.urls),
]
