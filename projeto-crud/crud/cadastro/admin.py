from django.contrib import admin

# Register your models here.
from .models import Registro, Conta

admin.site.register(Registro)

admin.site.register(Conta)
