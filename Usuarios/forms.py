from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg' , 'placeholder': 'Contraseña'}))


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Escriba el Nombre de Usuario', "id": "name"}))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg' , 'placeholder': 'Escriba la Contraseña'}))
    id_empleado = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': "id_empleado", 'type': 'hidden'}))
    id_rol = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': "id_rol", 'type': 'hidden'}))

