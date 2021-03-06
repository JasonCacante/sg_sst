# Generated by Django 3.2.7 on 2021-11-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0009_alter_rol_nombre_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='barrio',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Barrio'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='edad_emp',
            field=models.IntegerField(blank=True, null=True, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='email_emp',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_ing',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Ingreso'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='fecha_nac',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='genero_emp',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1, null=True, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='municipio',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Municipio'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='tipo_sangre_emp',
            field=models.CharField(blank=True, choices=[('O+', 'O Positivo'), ('O-', 'O Negativo'), ('A+', 'A Positivo'), ('A-', 'A Negativo'), ('B+', 'B Positivo'), ('B-', 'B Negativo'), ('AB+', 'AB Positivo'), ('AB-', 'AB Negativo')], max_length=3, null=True, verbose_name='Tipo de Sangre'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='turno_emp',
            field=models.CharField(blank=True, choices=[('Diurno', 'De 6:00 a las 20:00 horas'), ('Nocturno', 'De 20:00 a las 6:00 horas'), ('Mixto', 'De 6:00 a las 20:00 y de 20:00 a las 6:00 horas')], max_length=10, null=True, verbose_name='Turno'),
        ),
    ]
