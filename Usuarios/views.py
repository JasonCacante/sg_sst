from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Usuarios.models import Rol, Login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                rol = Rol.objects.get(usuariosgsst__id_login=usuario.id) #Esto trae el rol de la tabla usuariossgsst
                login(request, usuario)
                if rol.nombre_rol == "Admin":
                    return render(request, "Usuarios/inicio.html", {"rola": username, "password": password})
                elif rol.nombre_rol == "presiente":
                    return render(request, "Usuarios/inicio.html", {"rola": username, "password": password})
                else: 
                    return render(request, "Usuarios/login.html", {"rola": username, "password": password})
            else:
                messages.error(request, "Usuario o Contraseña erróneas, intentalo de nuevo")
                return redirect("usuarios")
        else:
            message = "Intentelo de nuevo, campos inválidos"
    else:
        form = LoginForm()
        message = "Método Get"
    return render(request, 'Usuarios/login.html', { "form": form, "message": message})

@login_required
def salir(request):
    logout(request)
    return redirect('home')