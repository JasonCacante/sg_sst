from django.contrib import admin
from .models import Empleado, Cargo, Area

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "cargo")

class CargoAdmin(admin.ModelAdmin):
    list_display = ("cargo", "area", "fecha_creacion", "salario")

class AreaAdmin(admin.ModelAdmin):
    list_display = ("area", "fecha_creacion")

admin.site.register(Area, AreaAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Cargo, CargoAdmin)