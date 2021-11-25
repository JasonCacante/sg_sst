from django.db import models
from django.db.models.deletion import CASCADE
import datetime



class Area(models.Model) :
    area = models.CharField(max_length=20)
    fecha_creacion = models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.area

class Cargo(models.Model) :
    cargo = models.CharField(max_length=20)
    area = models.ForeignKey(Area, on_delete=CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    salario = models.IntegerField()
    def __str__(self) :
        return self.cargo

class Empleado(models.Model) :
    nombres = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    cargo = models.ForeignKey(Cargo, on_delete=CASCADE)
    niveles = [('Primaria', 'Primaria'),
               ('Bachillerato', 'Bachillerato'),
               ('Técnico', 'Técnico'),
               ('Tecnológico', 'Tecnológico'),
               ('Universitario', 'Universitario'),
               ('Especialización', 'Universitario con especialización'),
               ('Maestría', 'Maestría'),
               ('Doctorado', 'Doctorado'),]
    estudios = models.CharField(max_length=25, choices= niveles, verbose_name='Nivel de estudio')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    def obtener_edad(self) :
        edad = datetime.date.today() - self.fecha_nacimiento
        return int((edad).days/365.25)
    
    identificacion = models.BigIntegerField(verbose_name='Número de identificación')
    gender = [('M', 'Masculino'),
              ('F', 'Femenino')]
    genero = models.CharField(max_length=1, choices=gender, verbose_name='Sexo biológico')
    sangre = [('O+', 'O+'),
              ('O-', 'O-'),
              ('A+', 'A+'),
              ('A-', 'A-'),
              ('B-', 'B-'),
              ('B+', 'B+'),
              ('AB-', 'AB-'),
              ('AB+', 'AB+')]
    tipo_sangre = models.CharField(max_length=3, choices=sangre, blank=True, null=True, verbose_name='Tipo de sangre')
    turno = models.CharField(max_length=30)
    fijo = models.CharField(max_length=10, blank=True, null=True)
    movil = models.CharField(max_length=10, blank=True, null=True)
    mail = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)
    direccion = models.CharField(max_length=50, verbose_name='Dirección - Barrio')
    municipio = models.CharField(max_length=30)
    estrato = models.SmallIntegerField(help_text='De 1 a 6', blank=True, null=True)
    etnias = [('Blanco', 'Blanco'),
              ('Mestizo', 'Mestizo'),
              ('Afrocolombiano', 'Afrocolombiano'),
              ('Mulato', 'Mulato'),
              ('Indígena', 'Indígena')]
    etnia = models.CharField(max_length=15, choices=etnias, blank=True, null=True)
    civil = [('Soltero', 'Soltero'),
              ('Casado', 'Casado'),
              ('Separado', 'Separado'),
              ('Unión Libre', 'Unión Libre'),
              ('Viudo', 'Viudo')]
    estado_civil = models.CharField(max_length=20, choices=civil, blank=True, null=True)
    hijos = models.SmallIntegerField(blank=True, null=True)
    tipo_contrato = models.CharField(max_length=20)
    enfermedad = models.CharField(max_length=25, blank=True, null=True)
    medicamentos = models.CharField(max_length=25, blank=True, null=True)
    induccion = models.BooleanField(blank=True, null=True, verbose_name='¿Recibió la inducción de SST?')
    fecha_retiro = models.DateField(blank=True, null=True)
    def rango(self) :
        tiempo_trabajo = datetime.date.today() - self.fecha_ingreso
        return int((tiempo_trabajo).days/365.25)
    vacuna = models.BooleanField(blank=True, null=True, verbose_name='¿Tiene esquema de vacunación?')
    carne = models.FileField(upload_to='carnet', verbose_name='Carnet', blank=True, null=True)
    estado = models.BooleanField()
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"{self.id} : {self.nombres} {self.apellidos}")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Contacto_Emergencia(models.Model) :
    empleado = models.OneToOneField(Empleado, on_delete=CASCADE)
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    parentezco = models.CharField(max_length=20)

class Seguridad_Social(models.Model) :
    empleado = models.OneToOneField(Empleado, on_delete=CASCADE)
    eps = models.CharField(max_length=20, verbose_name='EPS')
    afp = models.CharField(max_length=20, verbose_name='Fondo de pensiones')
    ccf = models.CharField(max_length=20, default='Comfenalco', verbose_name='Caja de compensación')
    arl = models.CharField(max_length=20, default='Bolivar', verbose_name='Aseguradora de Riesgos Laborales')

