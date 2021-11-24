from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Usuarios.models import Rol
from empleados.models import Empleado
from empleados.forms import EmpleadoForm


@login_required
def show_emp(request):
    usuario_id = request.user.id
    rol_name = Rol.objects.get(usuariosgsst__id_login=usuario_id).nombre_rol

    empleados = Empleado.objects.all()
    return render(request, 'empleados/inicio.html', { 'empleados': empleados, "rol": rol_name })

@login_required
def create_emp(request):
    usuario_id = request.user.id
    rol_name = Rol.objects.get(usuariosgsst__id_login=usuario_id).nombre_rol

    if request.method == 'POST':
            form = EmpleadoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('empleados')
    else:
        form = EmpleadoForm()
        return render(request, 'empleados/crear.html', {'form': form, "rol": rol_name})


@login_required
def delete_emp(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleados')

@login_required
def edit_emp(request, id):
    usuario_id = request.user.id
    rol_name = Rol.objects.get(usuariosgsst__id_login=usuario_id).nombre_rol

    if request.method == "POST":
        empleado = Empleado.objects.get(id=id)
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleados')
    else:
        empleado = Empleado.objects.get(id=id)
        form = EmpleadoForm(instance=empleado)
        return render(request, 'empleados/editar_empleado.html', {'form': form, "rol": rol_name})