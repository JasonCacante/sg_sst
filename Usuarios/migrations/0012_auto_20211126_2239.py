# Generated by Django 3.2.7 on 2021-11-27 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0011_alter_usuariosgsst_id_empleado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='area_cargo',
        ),
        migrations.RemoveField(
            model_name='documentacionempleado',
            name='id_emp',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='cargo_emp',
        ),
        migrations.DeleteModel(
            name='Area',
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='DocumentacionEmpleado',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
    ]