from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, registro,producto
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name="index"),

    path('login/', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('registro/', registro, name="registro"),
    path('producto/<codigo>', producto, name="producto"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)