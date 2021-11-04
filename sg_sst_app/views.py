from django.shortcuts import render
from Usuarios.models import Rol

def home(request):
    usuario_id = request.user.id
    rol = Rol.objects.get(usuariosgsst__id_login=usuario_id)
    return render(request, "sg_sst_app/home.html", {"rol": rol.nombre_rol})
