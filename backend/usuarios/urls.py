from django.urls import path, include

from .views import TeacherRegistrationView, ClientRegistrationView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ####        CLIENTE        ####

    ###     Registro Cliente     ###
    path('register/client/', ClientRegistrationView.as_view()),
    ###     Inicio de sesion de Cliente     ###
    path('client/login/', views.login_user, name='Login_Client'),
    ###     Muestra todos los perfiles de los Clientes     ###
    path('client/profile/', views.ProfilesViewClient.as_view(), name='Perfil_Client'),
    ###     Muestra perfil de un sólo Cliente por ID     ###
    path('client/profile/<int:id>', views.profile_client, name='Perfil_Teacher_ID'),

    ####        TEACHER        ####

    ###     Registro Teacher     ###
    path('register/teacher/', TeacherRegistrationView.as_view(), name='Registro_Teacher'),
    ###     Inicio de sesion de Teacher     ###
    path('teacher/login/', views.login_user, name='Login_Teacher'),
    ###     Muestra todos los perfiles de los Teachers    ###
    path('teacher/profile/', views.ProfilesViewTeacher.as_view(), name='Perfil_Teacher'),
    ###     Muestra perfil de un sólo Teacher por ID     ###
    path('teacher/profile/<int:id>', views.profile_teacher, name='Perfil_Teacher_ID'),

    ###     Muestra todos los Usuarios     ###
    path('users/', views.ProfilesViewUser.as_view(), name='Usuarios'),

    ####        CAMBIO DE CONTRASEÑA USUARIOS        ####
    path('user/reset_password/', include('django_rest_passwordreset.urls', namespace='reset_pass_client')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#hola gente