from django.urls import path
from documentacion.views import docEmpleado, index

urlpatterns = [
    path('', index, name='iniciodocs'),
    path('docsempleado', docEmpleado, name='docempleado'),
]

