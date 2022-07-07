from django.contrib import admin
from django.urls import path
from .views import index, registro
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name="index"),

    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('registro/', registro, name="registro"),
]