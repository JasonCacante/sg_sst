from django.urls import path
from Usuarios.views import (
    delete_user,
    edit_user,
    login_view,
    salir,
    show_users,
    create_user,
)

urlpatterns = [
    path("", show_users, name="usuarios"),
    path("<int:id>/", edit_user, name="usuario"),
    path("borrar/<int:id>/", delete_user, name="delete"),
    path("login/", login_view, name="login"),
    path("logout/", salir, name="logout"),
    path("nuevo/", create_user, name="nuevo"),
]
