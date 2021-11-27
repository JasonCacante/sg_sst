from django.db import models
from django.contrib.auth.models import User
from empleados.models import Empleado as Empleado2


class Comite(models.Model):
    comite = models.CharField(max_length=50, verbose_name="Comité")

    def __str__(self):
        return f"{self.comite}"

    class Meta:
        verbose_name = "comite"
        verbose_name_plural = "comites"


class Rol(models.Model):
    roles = [
        ("Admin", "Administrador"),
        ("Encar", "Encargado del SG-SST"),
        ("Pres1", "Presidente Comité COCOLA"),
        ("Pres2", "Presidente Comité COPASST"),
        ("Pres3", "Secretario Comité BE"),
    ]
    nombre_rol = models.CharField(
        max_length=50, choices=roles, verbose_name="Nombre Rol"
    )
    descripcion = models.TextField(verbose_name="Descripción")
    comite_id = models.ForeignKey(
        Comite,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Id Comité",
    )

    def __str__(self):
        return f"{self.nombre_rol} "

    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"


class Login(User):
    class Meta:
        proxy = True
        verbose_name = "credencial"
        verbose_name_plural = "credenciales"


class UsuarioSGSST(models.Model):
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")
    id_login = models.ForeignKey(
        Login, on_delete=models.CASCADE, verbose_name="Nombre de Usuario"
    )
    id_empleado = models.ForeignKey(
        Empleado2, on_delete=models.CASCADE, verbose_name="Nombre Empleado"
    )

    def __str__(self):
        return f"{self.id_rol} " + f"{self.id_login} " + f"{ self.id_empleado}"

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
