from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Declarando urls de usuarios
    path('', include('usuarios.urls'), name='Usuarios'),
]
