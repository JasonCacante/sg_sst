from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg' , 'placeholder': 'Contraseña'}))
