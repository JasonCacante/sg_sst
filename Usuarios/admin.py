from django.contrib import admin

from .models import Empleado, Rol, Login, UsuarioSGSST

# Register your models here.

class EmpleadosAdmin(admin.ModelAdmin):
    search_fields = ("apellido1_emp", "cedula_emp")
    list_display = ("cedula_emp", "nombre1_emp", "apellido1_emp", "celular_emp", "cargo_emp")

class RolsAdmin(admin.ModelAdmin):
    list_display = ("nombre_rol", "descripcion", "comite_id")

class LoginAdmin(admin.ModelAdmin):
    list_display = ("user", "password")

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("id_rol", "id_login", "id_empleado")

admin.site.register(Rol, RolsAdmin)
admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Login, LoginAdmin)
admin.site.register(UsuarioSGSST, UsuariosAdmin)