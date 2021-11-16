from django.contrib import admin
from .models import TipoDoc, DocsEmpleado, DocsEmpresa

# Register your models here.

class TipoDocAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo", "fecha_creacion")

class DocsEmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "documento", "fecha_vencimiento")

class DocsEmpresaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "documento", "fecha_vencimiento")

admin.site.register(TipoDoc, TipoDocAdmin)
admin.site.register(DocsEmpleado, DocsEmpleadoAdmin)
admin.site.register(DocsEmpresa, DocsEmpresaAdmin)