from django.shortcuts import render
from django.views import View
from gestion_clinica.models import Empleado, Paciente, Proveedor   
from gestion_clinica.form import EmpleadoForm, PacienteForm, ProveedorForm, Buscar
                               


class ListarEmpleados(View):
    template_name = "gestion_clinica/lista_de_empleados.html"

    def get(self, request):
        empleados = Empleado.objects.all()
        return render(request, self.template_name, {"empleados": empleados})


class CargarEmpleados(View):
    template_name = "gestion_clinica/carga_de_empleados.html"
    form_class = EmpleadoForm
    initial = {"nombre": "", "apellido": "", "fecha_de_nacimiento": "", "contacto_telefonico": "", "contacto_email": ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
            
        return render(request, self.template_name, {"form": form})


# Ahora viene la parte de pacientes

class ListarPacientes(View):
    template_name = "gestion_clinica/lista_de_pacientes.html"

    def get(self, request):
        pacientes = Paciente.objects.all()
        return render(request, self.template_name, {"pacientes": pacientes})


class CargarPacientes(View):
    template_name = "gestion_clinica/carga_de_pacientes.html"
    form_class = PacienteForm
    initial = {"nombre": "", "apellido": "", "fecha_de_nacimiento": "", "contacto_telefonico": "", "contacto_email": ""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})


# Ahora viene la parte de proveedores

class ListarProveedores(View):
    template_name = "gestion_clinica/lista_de_Proveedores.html"

    def get(self, request):
        proveedor = Proveedor.objects.all()
        return render(request, self.template_name, {"proveedores": proveedor})


class CargarProveedores(View):
    template_name = "gestion_clinica/carga_de_proveedores.html"
    form_class = ProveedorForm
    initial = {"nombre": "", "contacto_telefonico":"", "contacto_email":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self,request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.save()
            form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

class BuscarEmpleado(View):

    form_class = Buscar
    template_name = 'gestion_clinica/buscar_empleado.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_empleados = Empleado.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_empleados':lista_empleados})
        return render(request, self.template_name, {"form": form})