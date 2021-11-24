# Generated by Django 3.2.7 on 2021-11-16 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('salario', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.area')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('estudios', models.CharField(choices=[('Primaria', 'Primaria'), ('Bachillerato', 'Bachillerato'), ('Técnico', 'Técnico'), ('Tecnológico', 'Tecnológico'), ('Universitario', 'Universitario'), ('Especialización', 'Universitario con especialización'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=25, verbose_name='Nivel de estudio')),
                ('fecha_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('identificacion', models.BigIntegerField(verbose_name='Número de identificación')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Sexo biológico')),
                ('tipo_sangre', models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=3, null=True, verbose_name='Tipo de sangre')),
                ('turno', models.CharField(max_length=30)),
                ('fijo', models.CharField(blank=True, max_length=10, null=True)),
                ('movil', models.CharField(blank=True, max_length=10, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('direccion', models.CharField(max_length=50, verbose_name='Dirección - Barrio')),
                ('municipio', models.CharField(max_length=30)),
                ('estrato', models.SmallIntegerField(blank=True, help_text='De 1 a 6', null=True)),
                ('etnia', models.CharField(blank=True, choices=[('Blanco', 'Blanco'), ('Mestizo', 'Mestizo'), ('Afrocolombiano', 'Afrocolombiano'), ('Mulato', 'Mulato'), ('Indígena', 'Indígena')], max_length=15, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Separado', 'Separado'), ('Unión Libre', 'Unión Libre'), ('Viudo', 'Viudo')], max_length=20, null=True)),
                ('hijos', models.SmallIntegerField(blank=True, null=True)),
                ('tipo_contrato', models.CharField(max_length=20)),
                ('enfermedad', models.CharField(blank=True, max_length=25, null=True)),
                ('medicamentos', models.CharField(blank=True, max_length=25, null=True)),
                ('induccion', models.BooleanField(blank=True, null=True, verbose_name='¿Recibió la inducción de SST?')),
                ('fecha_retiro', models.DateField(blank=True, null=True)),
                ('vacuna', models.BooleanField(blank=True, null=True, verbose_name='¿Tiene esquema de vacunación?')),
                ('carne', models.FileField(blank=True, null=True, upload_to='')),
                ('estado', models.BooleanField()),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empleados.cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Seguridad_Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eps', models.CharField(max_length=20, verbose_name='EPS')),
                ('afp', models.CharField(max_length=20, verbose_name='Fondo de pensiones')),
                ('ccf', models.CharField(default='Comfenalco', max_length=20, verbose_name='Caja de compensación')),
                ('arl', models.CharField(default='Bolivar', max_length=20, verbose_name='Aseguradora de Riesgos Laborales')),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto_Emergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=10)),
                ('parentezco', models.CharField(max_length=20)),
                ('empleado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empleados.empleado')),
            ],
        ),
    ]