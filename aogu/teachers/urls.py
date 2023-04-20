from django.urls import path
from .views import register_teacher

urlpatterns = [
    path('', register_teacher, name='register_teacher'),
]