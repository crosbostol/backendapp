from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.conf import settings


###     VARIABLES GLOBALES     ###
expertise_status = [
    ('L', 'Legal'),
    ('F', 'Financiera')
]

careers_status = [
    ('abogado', 'Derecho'),
    ('ingeniero economico', 'Ingeniero en economia'),
    ('Ingeniero industrial', 'Ingeniero industrial'),
    ('Ingeniero informatico', 'Ingeniero en informatica'),
]

# Create your models here.

###     TABLA USER     ###
class User(AbstractUser):
    ###     VARIABLES BOOLEANAS     ###
    is_client = models.BooleanField(default=False, verbose_name='Cliente')
    is_teacher = models.BooleanField(default=False, verbose_name='Teacher')
    ###     ATRIBUTOS     ###
    email = models.EmailField(max_length=150, unique=True, verbose_name="Correo")
    
    ###     METODO DE LOGEO     ###
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


###     TABLA CLIENTE     ###
class Client(models.Model):
    ###     HEREDA DE LA TABLA USER     ###
    client= models.OneToOneField(
      User, on_delete=models.CASCADE, blank=True, null=True)
    ###     ATRIBUTOS     ###
    rut = models.CharField(max_length=12, verbose_name='RUT')
    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name="Telefono")

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Creacion")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha Actualizacion")

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'

    def __str__(self):
        return self.client.username


###     TABLA TEACHER     ###
class Teacher(models.Model):
    ###     HEREDA DE LA TABLA USER     ###
    teacher = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True)
    ###     ATRIBUTOS     ###
    rut = models.CharField(max_length=12, verbose_name='RUT')
    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name="Telefono")
    high_school = models.CharField(max_length=50, verbose_name="Institucion Educacion Superior")
    docfile = models.FileField(upload_to='documents/', verbose_name='Documento')
    img = models.ImageField(upload_to='images/', verbose_name='Imagen Perfil')
    expertise = models.CharField(
        max_length=1,
        null=False, blank=False,
        choices=expertise_status,
        default=""
    )
    careers= models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=careers_status,
        default=""
    )

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha Creacion")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha Actualizacion")
    
    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'
        ordering = ('-created_at',)
    
    def __str__(self):
      return self.teacher.username  