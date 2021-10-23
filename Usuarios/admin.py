from django.contrib import admin

from .models import Usuario, Rol, Login

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    search_fields = ("codigo", "cedula")
    list_display = ("codigo", "primer_nombre", "primer_apellido", "id_rol", "id_login")

class RolsAdmin(admin.ModelAdmin):
    search_fields = ("id_rol", "nombre_rol")

class LoginAdmin(admin.ModelAdmin):
    search_fields = ("nombre_usuario",)

admin.site.register(Rol, RolsAdmin)
admin.site.register(Usuario, UsuariosAdmin)
admin.site.register(Login, LoginAdmin)