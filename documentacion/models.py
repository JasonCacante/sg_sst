from django.db import models
from empleados.models import Empleado


class TipoDoc(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo de documento"
        verbose_name_plural = "Tipos de documentos"


class DocsEmpleado(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Archivo")
    documento = models.FileField(
        upload_to="documentos", verbose_name="Documento", blank=True, null=True
    )
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    tipo_doc = models.ForeignKey(
        TipoDoc, on_delete=models.CASCADE, verbose_name="Tipo de documento"
    )
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    observaciones = models.TextField(
        max_length=500, verbose_name="Observaciones", blank=True, null=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Documento de empleado"
        verbose_name_plural = "Documentos de empleado"


class DocsEmpresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Archivo")
    documento = models.FileField(
        upload_to="docsempresa", verbose_name="Documento", blank=True, null=True
    )
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    tipo_doc = models.ForeignKey(
        TipoDoc, on_delete=models.CASCADE, verbose_name="Tipo de documento"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion = models.TextField(
        max_length=500, verbose_name="Descripción", blank=True, null=True
    )
    firma = models.CharField(
        max_length=100, verbose_name="Firma", blank=True, null=True
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    observaciones = models.TextField(
        max_length=500, verbose_name="Observaciones", blank=True, null=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Documento de empresa"
        verbose_name_plural = "Documentos de empresa"
