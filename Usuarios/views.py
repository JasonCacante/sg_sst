from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Usuarios.models import Rol, Login, UsuarioSGSST
from empleados.models import Empleado
from .forms import LoginForm, CreateUserForm
from django.contrib.auth.hashers import make_password


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                rol = Rol.objects.get(usuariosgsst__id_login=usuario.id) #Esto trae el rol de la tabla usuariossgsst
                nombre_rol = rol.nombre_rol
                login(request, usuario)
                if nombre_rol == "Admin":
                    return redirect('usuarios')
                elif nombre_rol == "Encar":
                    return redirect('iniciodocs')
                elif nombre_rol == "Pres    1":
                    return render(request, "Usuarios/inicio.html")
                elif nombre_rol == "Pres2":
                    return render(request, "Usuarios/inicio.html")
                elif nombre_rol == "Pres3":
                    return render(request, "Usuarios/inicio.html")
                else: 
                    return render(request, "Usuarios/login.html")
            else:
                messages.error(request, "Usuario o Contraseña erróneas, intentalo de nuevo")
                return redirect("login")
        else:
            messages.error(request, "Intentelo de nuevo, campos inválidos")
            return redirect("login")
    else:
        form = LoginForm()
    return render(request, 'Usuarios/login.html', { "form": form })


@login_required
def salir(request):
    logout(request)
    return redirect('home')


@login_required
def show_users(request):
    usuario_id = request.user.id
    rol_name = Rol.objects.get(usuariosgsst__id_login=usuario_id).nombre_rol
    
    usuarios = Login.objects.all()
    return render(request, 'Usuarios/inicio.html', { 'usuarios': usuarios, "rol": rol_name })


@login_required
def edit_user(request,id):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            id_empleado = form.cleaned_data['id_empleado']
            id_rol = form.cleaned_data['id_rol']
            empleado = Empleado.objects.get(id=id_empleado)
            first_name = empleado.nombres
            last_name = empleado.apellidos

            login = Login.objects.get(id=str(id))
            login.username = username
            login.set_password(make_password(password))
            login.first_name = first_name
            login.last_name = last_name
            login.save()

            rol = Rol.objects.get(id=id_rol)

            usuario = UsuarioSGSST.objects.get(id_login=login)
            usuario.id_rol = rol
            usuario.id_empleado = empleado
            usuario.save()
        else:
            messages.error(request, "Tienes que seleccionar todos los campos. Intentalo de nuevo")
        return redirect('usuarios')
    else:
        form = CreateUserForm(request.GET)
        login = Login.objects.get(id=str(id))
        form.fields['username'].widget.attrs['placeholder']=login.username
        rol = Rol.objects.get(usuariosgsst__id_login=str(id))
        empleado = Empleado.objects.get(usuariosgsst__id_login=str(id))
        empleados = Empleado.objects.all()
        roles = Rol.objects.all()
        ctx = {
            "form": form,
            "empleado": empleado,
            "rol": rol,
            "login": login,
            "roles": roles,
            "empleados": empleados,
        }
        return render(request, 'Usuarios/editar.html', ctx)


@login_required
def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            nombre_usuario = Login.objects.filter(username=username)

            if nombre_usuario:
                messages.error(request, "El nombre usuario ya existe, ingresa otro")
                return redirect('nuevo')

            password = form.cleaned_data['password']
            id_empleado = form.cleaned_data['id_empleado']
            id_rol = form.cleaned_data['id_rol']
            empleado = Empleado.objects.get(id=id_empleado)
            first_name = empleado.nombres
            last_name = empleado.apellidos
            login = Login(
                username=username,
                password=make_password(password),
                is_staff=False,
                first_name=first_name,
                last_name=last_name
            )
            login.save()
            rol = Rol.objects.get(id=id_rol)
            usuario = UsuarioSGSST(
                id_rol=rol,
                id_empleado=empleado,
                id_login=login
            )
            usuario.save()
        else:
            messages.error(request, "Tienes que seleccionar todos los campos. Intentalo de nuevo")
        return redirect('nuevo')
    else:
        form = CreateUserForm(request.GET)
        empleados = Empleado.objects.all()
        roles = Rol.objects.all()
        ctx = {
            "form": form,
            "empleados": empleados,
            "roles": roles,
        }
        return render(request, 'Usuarios/crear_usuario.html', ctx)


@login_required
def delete_user(request, id):
    login = Login.objects.get(id=str(id))
    login.delete()
    return redirect('usuarios')

