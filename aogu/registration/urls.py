from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView



urlpatterns = [
    path('', views.login, name='login'),
    path("register", views.register, name="register"),
    path('change_password/', PasswordChangeView.as_view(template_name='change_password.html')),
    path('profile/', views.profile, name='profile'),
    path('change_login/', views.change_login, name='change_login'),
    path('choice/', views.choice, name='choice'),
]   




