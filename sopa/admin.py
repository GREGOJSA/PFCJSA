from django.contrib import admin
from .models import empresas, usuarios, encuestas
# Register your models here.

class empresasAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'departamento', 'tutor')
    list_filter = ('nombre_empresa', 'departamento', 'tutor')
    search_fields = ('nombre_empresa', 'departamento', 'tutor')


class encuestasAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'departamento', 'tutor', 'user')
    list_display_links= ('nombre_empresa', 'departamento', 'tutor', 'user')
    list_filter = ('nombre_empresa', 'departamento', 'tutor', 'user')
    search_fields = ('nombre_empresa', 'departamento', 'tutor', 'user')

class usuariosAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','grado')
    list_filter = ('username', 'first_name', 'last_name','grado')
    search_fields = ('username', 'first_name', 'last_name','grado')


admin.site.register(usuarios, usuariosAdmin)
admin.site.register(empresas, empresasAdmin)
admin.site.register(encuestas, encuestasAdmin)
