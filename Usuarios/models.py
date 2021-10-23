from django.db import models


class Rol(models.Model):
    id_rol=models.SmallIntegerField(primary_key=True, verbose_name="Código")
    nombre_rol=models.CharField(max_length=50, verbose_name="Nombre Rol")
    def __str__(self):
        return(
            f"{self.nombre_rol} "
        )



class Login(models.Model):
    id_login=models.SmallIntegerField(primary_key=True, verbose_name="Código")
    nombre_usuario=models.CharField(max_length=50, verbose_name="Nombre Usuario")
    password=models.CharField(max_length=50, verbose_name="Contraseña")
    id_rol=models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")
    def __str__(self):
        return(
            f"{self.nombre_usuario} "
        )



class Usuario(models.Model):
    codigo=models.SmallIntegerField(primary_key=True, verbose_name="Código")
    primer_nombre=models.CharField(max_length=30, verbose_name="Primer Nombre")
    segundo_nombre=models.CharField(max_length=30, blank=True, verbose_name="Segundo Nombre")
    primer_apellido=models.CharField(max_length=30, verbose_name="Primer Apellido")
    segundo_apellido=models.CharField(max_length=30, verbose_name="Segundo Apellido")
    cedula=models.CharField(max_length=10, verbose_name="Cédula")
    telefono=models.CharField(max_length=10, blank=True, verbose_name="Teléfono")
    celular=models.CharField(max_length=10, verbose_name="Celular")
    direccion=models.CharField(max_length=30, verbose_name="Dirección")
    id_rol=models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Código Rol")
    id_login=models.ForeignKey(Login, on_delete=models.CASCADE, verbose_name="Código Login")

    def __str__(self):
        return(
            f"{self.primer_nombre} "
            + f"{self.segundo_nombre} "
            + f"{self.primer_apellido} "
            + f"{ self.segundo_apellido}"
        )

