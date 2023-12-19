from django.contrib import admin
from django.urls import path, include
from project import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('', include('project.urls')),
]