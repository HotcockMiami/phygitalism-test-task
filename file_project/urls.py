"""
Здесь описываются URL для всего проекта, в рамках данного
мы просто добавим уже ранее описанные из ../file_app/urls.py
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('file_app.urls')) 
]
