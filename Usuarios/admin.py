from django.contrib import admin

from .models import Rol, UsuarioSGSST

# Register your models here.


class RolsAdmin(admin.ModelAdmin):
    list_display = ("nombre_rol", "descripcion", "comite_id")


class UsuariosAdmin(admin.ModelAdmin):
    list_display = ("id_rol", "id_login", "id_empleado")


admin.site.register(Rol, RolsAdmin)
admin.site.register(UsuarioSGSST, UsuariosAdmin)
