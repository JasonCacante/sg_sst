from django.urls import path
from Usuarios.views import (
    login_view,
)

urlpatterns = [
    path("", login_view, name="usuarios"),
]
