from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    contacto_tel = models.PositiveIntegerField()
    contacto_email = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Contacto telefonico: {self.contacto_tel}, Contacto email: {self.contacto_email}'


class Paciente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()
    contacto_tel = models.PositiveIntegerField()
    contacto_email = models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de nacimiento: {self.fecha_de_nacimiento}, Contacto telefonico: {self.contacto_tel}, Contacto email: {self.contacto_email}'


class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=10)
    contacto_tel = models.PositiveIntegerField()
    contacto_email = models.EmailField()
    
    def __str__(self):
        return f'Nombre:{self.nombre_empresa}, Contacto telefonico: {self.contacto_tel}, Contacto email: {self.contacto_email}'
    
