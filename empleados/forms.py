from django import forms
from empleados.models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = { 
            'carne': forms.FileInput(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Seleccione un archivo', "id": "name"}),
        }