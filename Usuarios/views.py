from django.shortcuts import redirect, render
from django.contrib import messages
from Usuarios.models import Login, Rol
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                usuario = Login.objects.get(user=username)
            except Login.DoesNotExist:
                messages.error(request, "El usuario no existe, intentalo de nuevo o contacta al administrador")
                return redirect("usuarios")
            if password == usuario.password:
                rol = Rol.objects.get(usuariosgsst__id_login=usuario.id) #Esto trae el rol de la tabla usuariossgsst
                if rol.nombre_rol == "Admin":
                    return render(request, "Usuarios/inicio.html", {"rola": username, "password": password})
                elif rol.nombre_rol == "presiente":
                    return render(request, "Usuarios/inicio.html", {"rola": username, "password": password})
                else: 
                    return render(request, "Usuarios/login.html", {"rola": username, "password": password})
            else:
                messages.error(request, "La contraseña no corresponde con el usuario ingresado")
                return redirect("usuarios")
        else:
            message = "Intentelo de nuevo, campos inválidos"
    else:
        form = LoginForm()
        message = "Método Get" 
    return render(request, 'Usuarios/login.html', { "form": form, "message": message})
