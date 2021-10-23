from django.shortcuts import render
from .forms import LoginForm

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Form data is valid
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return render(request, "Usuarios/inicio.html", {"user": username, "password": password})
        else:
            message = "Intentelo de nuevo, campos inválidos"
    else:
        form = LoginForm()
        message = "Método Get"
    return render(request, 'Usuarios/login.html', { "form": form, "message": message})
