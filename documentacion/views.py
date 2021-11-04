from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Usuarios.models import Rol

@login_required
def index(request):
    usuario_id = request.user.id
    rol = Rol.objects.get(usuariosgsst__id_login=usuario_id)
    return render(request, 'Usuarios/inicio.html', {"rol": rol.nombre_rol})
