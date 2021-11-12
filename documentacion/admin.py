from django.contrib import admin
from .models import TipoDoc

# Register your models here.

class TipoDocAdmin(admin.ModelAdmin):
    list_display = ("nombre", "activo", "fecha_creacion")

admin.site.register(TipoDoc, TipoDocAdmin)