from django.contrib import admin
from django.urls import path, include, re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
]
