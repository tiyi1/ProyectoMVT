from django.contrib import admin
from gestion_clinica.models import Empleado, Paciente, Proveedor

admin.site.register(Empleado)
admin.site.register(Paciente)
admin.site.register(Proveedor)