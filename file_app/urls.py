from django.urls import path
from .views import FilesView # Добавляем "вьюху" для добавления её в URL паттерны

app_name = "file_app"

urlpatterns = [
    path('files/', FilesView.as_view()),
]