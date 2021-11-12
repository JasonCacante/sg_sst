from django import forms
from django.forms import widgets
from documentacion.models import DocsEmpleado

class LoadDocuments(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoadDocuments, self).__init__(*args, **kwargs)
        self.fields['tipo_doc'].empty_label = 'Seleccione el tipo de documento'
        self.fields['empleado'].empty_label = 'Seleccione el propietario del documento'

    class Meta:
        model = DocsEmpleado
        fields = '__all__'
        widgets = { 
            'fecha_vencimiento': forms.DateInput(attrs={'class':'form-control datetimepicker', 'type':'date'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Escriba el Nombre del Documento', "id": "name"}),
            'tipo_doc': forms.Select(attrs={'class': 'form-select form-select-lg mb-3', "id": "name"}),
            'empleado': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check form-check-input',
                "id": "activo",
                }),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'widht': '50%', 'height': '30%', 'placeholder': 'Escriba las observaciones del documento'
                }),
            'documento': forms.FileInput(attrs={'class': 'form-control form-control-lg ', 'placeholder': 'Seleccione un archivo', "id": "name"}),
        }
