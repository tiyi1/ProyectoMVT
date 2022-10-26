"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('gestion_clinica/', include('gestion_clinica.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion_clinica.views import (ListarEmpleados, CargarEmpleados, ListarPacientes, CargarPacientes, ListarProveedores, CargarProveedores, BuscarEmpleado)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', ListarEmpleados.as_view()),
    path('empleados/cargar', CargarEmpleados.as_view()),
    path('pacientes/', ListarPacientes.as_view()),
    path('pacientes/cargar', CargarPacientes.as_view()),
    path('proveedores/', ListarProveedores.as_view()),
    path('proveedores/cargar', CargarProveedores.as_view()),
    path('empleados/buscar_empleado', BuscarEmpleado.as_view()),
    
]
