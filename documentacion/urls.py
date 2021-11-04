from django.urls import path
from documentacion.views import index

urlpatterns = [
    path('', index, name='iniciodocs'),
]

