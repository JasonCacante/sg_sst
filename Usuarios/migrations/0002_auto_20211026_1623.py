# Generated by Django 3.2.7 on 2021-10-26 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id_rol',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Rol',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
