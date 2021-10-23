from django.urls import path
from Usuarios.views import (
    loginView,
)

urlpatterns = [
    path("", loginView, name="loginView"),
]
