from django.shortcuts import redirect, render
from django.contrib import messages
from Usuarios.models import Login, Rol
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Form data is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                usuario = Login.objects.get(nombre_usuario=username)
            except Login.DoesNotExist:
                messages.error(request, "El usuario no existe, intentalo de nuevo o contacta al administrador")
                return redirect("usuarios")
            if password == usuario.password:
                rol = Rol.objects.get(id_rol=usuario.id_rol_id)
                if rol.nombre_rol == "admin":
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
