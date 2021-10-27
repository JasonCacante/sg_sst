from django.urls import path
from Usuarios.views import (
    login_view,
    salir,
    show_users,
    create_user,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", salir, name="logout"),
    path("lista/", show_users, name="usuarios"),
    path("nuevo/", create_user, name="nuevos"),
]
