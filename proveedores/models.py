from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    nit = models.CharField(max_length=50, verbose_name="NIT")
    certificado_arl = models.FileField(
        verbose_name="Certificado ARL", blank=True, null=True
    )
    telefono1 = models.CharField(
        max_length=50, verbose_name="Teléfono 1", blank=True, null=True
    )
    seguridad_social = models.CharField(
        max_length=50, verbose_name="Seguridad Social", blank=True, null=True
    )
    es_autorizado = models.BooleanField(default=True, verbose_name="¿Es autorizado?")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    ficha_seguridad_producto = models.FileField(
        upload_to="ficha_seguridad_producto",
        blank=True,
        null=True,
        verbose_name="Ficha de Seguridad Producto",
    )
    telefono2 = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Teléfono 2"
    )
    email = models.EmailField(
        max_length=50, blank=True, null=True, verbose_name="Email"
    )
    tipo_empresa = models.CharField(
        max_length=50, blank=True, null=True, verbose_name="Tipo de Empresa"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"


class Elemento(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Elemento"
        verbose_name_plural = "Elementos"


class Elementos_Proveedor(models.Model):
    proveedor = models.ForeignKey(
        Proveedor, on_delete=models.CASCADE, verbose_name="Proveedor"
    )
    elemento = models.ForeignKey(
        Elemento, on_delete=models.CASCADE, verbose_name="Elemento"
    )
    activo = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )
    vida_util = models.IntegerField(verbose_name="Vida útil", blank=True, null=True)

    def __str__(self):
        return self.proveedor.nombre + " - " + self.elemento.nombre

    class Meta:
        verbose_name = "Elemento Proveedor"
        verbose_name_plural = "Elementos Proveedores"
