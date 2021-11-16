from django.urls import path
from documentacion.views import docEmpleado, index, docEmpresa

urlpatterns = [
    path('', index, name='iniciodocs'),
    path('docsempleado', docEmpleado, name='docempleado'),
    path('docsempresa', docEmpresa, name='docempresa'),
]

