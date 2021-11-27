# Generated by Django 3.2.7 on 2021-11-26 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Elemento',
                'verbose_name_plural': 'Elementos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('nit', models.CharField(max_length=50, verbose_name='NIT')),
                ('certificado_arl', models.FileField(blank=True, null=True, upload_to='', verbose_name='Certificado ARL')),
                ('telefono1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono 1')),
                ('seguridad_social', models.CharField(blank=True, max_length=50, null=True, verbose_name='Seguridad Social')),
                ('es_autorizado', models.BooleanField(default=True, verbose_name='¿Es autorizado?')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('ficha_seguridad_producto', models.FileField(blank=True, null=True, upload_to='ficha_seguridad_producto', verbose_name='Ficha de Seguridad Producto')),
                ('telefono2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono 2')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('tipo_empresa', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Empresa')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Elementos_Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('vida_util', models.IntegerField(blank=True, null=True, verbose_name='Vida útil')),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.elemento', verbose_name='Elemento')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name': 'Elemento Proveedor',
                'verbose_name_plural': 'Elementos Proveedores',
            },
        ),
    ]
