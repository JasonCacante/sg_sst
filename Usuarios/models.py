from django.db import models
from django.contrib.auth.models import User


class Area(models.Model):
    areas=models.CharField(max_length=50, verbose_name="Areas")

    def __str__(self):
        return(
            f"{self.areas}"
        )

    class Meta:
        verbose_name  = "area" 
        verbose_name_plural = "areas" 


class Cargo(models.Model):
    cargo=models.CharField(max_length=30,verbose_name="Cargo")
    responsabilidades=models.TextField(verbose_name="Responsabilidades")
    area_cargo=models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área")

    def __str__(self):
        return(
            f"{self.cargo}"
        )

    class Meta:
        verbose_name  = "cargo" 
        verbose_name_plural = "cargos"


class Empleado(models.Model):
    nombre1_emp=models.CharField(max_length=12, verbose_name="Primer Nombre")
    nombre2_emp=models.CharField(max_length=12, verbose_name="Segundo Nombre")
    apellido1_emp=models.CharField(max_length=12, verbose_name="Primer Apellido")
    apellido2_emp=models.CharField(max_length=12, verbose_name="Segundo Apellido")
    cedula_emp=models.BigIntegerField(verbose_name="Cédula")
    telefono_emp=models.CharField(max_length=10, blank=True, verbose_name="Teléfono")
    celular_emp=models.CharField(max_length=10, verbose_name="Celular")
    direccion_emp=models.CharField(max_length=50, verbose_name="Dirección")
    niveles_edu = [
        ('Básica', 'Educación Básica'),
        ('Bachiller', 'Educación Media'),
        ('Profesional', 'Educación Superior'),
    ]
    nivel_emp=models.CharField(max_length=12, choices=niveles_edu, verbose_name='Nivel de Educación')
    cargo_emp=models.ForeignKey(Cargo, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Cargo")
    fecha_ing=models.DateField(verbose_name="Fecha de Ingreso",  blank=True, null=True)
    fecha_nac=models.DateField(verbose_name="Fecha de Nacimiento",  blank=True, null=True)
    edad_emp=models.IntegerField(verbose_name="Edad",  blank=True, null=True)
    genero = [
        ('M', 'Masculino'), 
        ('F', 'Femenino'), 
        ('O', 'Otro')
    ]
    genero_emp=models.CharField(max_length=1, choices=genero, verbose_name="Género",  blank=True, null=True)
    tipo_sangre = [
        ('O+', 'O Positivo'), ('O-', 'O Negativo'), ('A+', 'A Positivo'), ('A-', 'A Negativo'), ('B+', 'B Positivo'), ('B-', 'B Negativo'), ('AB+', 'AB Positivo'), ('AB-', 'AB Negativo')
    ]

    tipo_sangre_emp=models.CharField(max_length=3, choices=tipo_sangre, verbose_name="Tipo de Sangre",  blank=True, null=True)
    turnos = [ 
        ( 'Diurno', 'De 6:00 a las 20:00 horas' ), ( 'Nocturno', 'De 20:00 a las 6:00 horas' ), ( 'Mixto', 'De 6:00 a las 20:00 y de 20:00 a las 6:00 horas' ) 
    ]
    turno_emp=models.CharField(max_length=10, choices=turnos, verbose_name="Turno",  blank=True, null=True)
    email_emp = models.EmailField(verbose_name="Correo Electrónico", blank=True, null=True)
    barrio = models.CharField(max_length=50, verbose_name="Barrio", blank=True, null=True)
    municipio = models.CharField(max_length=50, verbose_name="Municipio", blank=True, null=True)

    def __str__(self):
        return(
            f"{self.nombre1_emp} "
        )

    class Meta:
        verbose_name  = "empleado"
        verbose_name_plural = "empleados" 


class DocumentacionEmpleado(models.Model):
    nombre_doc=models.CharField(max_length=50, verbose_name="Nombre Documentación")
    path_doc=models.CharField(max_length=100, verbose_name="Ruta Documento")
    fecha_mod=models.DateField(auto_now=True)
    id_emp=models.ForeignKey(Empleado,on_delete=models.CASCADE, verbose_name="Id Empleado")

    def __str__(self):
        return(
            f"{self.nombre_doc}"
        )

    class Meta:
        verbose_name  = "docuempleado" 
        verbose_name_plural = "docuempleados"


class Comite(models.Model):
    comite=models.CharField(max_length=50, verbose_name="Comité")
    def __str__(self):
        return(
            f"{self.comite}"
        )

    class Meta:
        verbose_name  = "comite" 
        verbose_name_plural = "comites"


class Rol(models.Model):
    roles = [
        ('Admin', 'Administrador'),
        ('Encar', 'Encargado del SG-SST'),
        ('Pres1', 'Presidente Comité COCOLA'),
        ('Pres2', 'Presidente Comité COPASST'),
        ('Pres3', 'Secretario Comité BE'),
    ]
    nombre_rol=models.CharField(max_length=50, choices=roles, verbose_name="Nombre Rol")
    descripcion=models.TextField(verbose_name="Descripción")
    comite_id=models.ForeignKey(Comite,on_delete=models.CASCADE, blank=True, null=True, verbose_name="Id Comité")

    def __str__(self):
        return(
            f"{self.nombre_rol} "
        )

    class Meta:
        verbose_name  = "rol" 
        verbose_name_plural = "roles"


class Login(User):

    class Meta:
        proxy = True
        verbose_name  = "credencial" 
        verbose_name_plural = "credenciales"


class UsuarioSGSST(models.Model):
    id_rol=models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name="Rol")
    id_login=models.ForeignKey(Login, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    id_empleado=models.ForeignKey(Empleado, on_delete=models.CASCADE, verbose_name="Nombre Empleado")

    def __str__(self):
        return(
            f"{self.id_rol} "
            + f"{self.id_login} "
            + f"{ self.id_empleado}"
        )

    class Meta:
        verbose_name  = "usuario" 
        verbose_name_plural = "usuarios"
