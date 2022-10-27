from django import forms
from gestion_clinica.models import Empleado, Paciente, Proveedor

class EmpleadoForm(forms.ModelForm):

    fecha_de_nacimiento = forms.DateField(label="Fecha de nacimiento", input_formats=["%d/%m/%y"],
    widget=forms.TextInput(attrs={'placeholder': '10/11/90'}))

    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento','contacto_tel','contacto_email' ]


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento','contacto_tel','contacto_email' ]


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre_empresa', 'contacto_tel', 'contacto_email']


class Buscar(forms.Form):
      nombre = forms.CharField(max_length=100)