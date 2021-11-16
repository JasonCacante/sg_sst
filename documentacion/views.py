from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from documentacion.forms import LoadDocuments, LoadDocumentsEmpresa
from Usuarios.models import Rol

@login_required
def index(request):
    usuario_id = request.user.id
    rol = Rol.objects.get(usuariosgsst__id_login=usuario_id)
    return render(request, 'documentacion/index.html', {"rol": rol.nombre_rol})

@login_required
def docEmpleado(request):
    usuario_id = request.user.id
    rol = Rol.objects.get(usuariosgsst__id_login=usuario_id)
    if request.method == 'POST':
        form = LoadDocuments(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('iniciodocs')
    else:
        form = LoadDocuments(request.GET)
        return render(request, 'documentacion/docEmpleado.html', {'form': form, "rol": rol.nombre_rol})

@login_required
def docEmpresa(request):
    usuario_id = request.user.id
    rol = Rol.objects.get(usuariosgsst__id_login=usuario_id)
    if request.method == 'POST':
        form = LoadDocumentsEmpresa(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('iniciodocs')
    else:
        form = LoadDocumentsEmpresa(request.GET)
        return render(request, 'documentacion/docEmpresa.html', {'form': form, "rol": rol.nombre_rol})
