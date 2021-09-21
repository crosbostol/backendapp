from django.contrib import admin

from .models import User, Teacher, Client
# Register your models here.

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Client)