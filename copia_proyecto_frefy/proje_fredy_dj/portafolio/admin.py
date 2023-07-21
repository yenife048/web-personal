from django.contrib import admin
from .models import project

#se importa el modelo que se creo (nombre de la clase)
# Register your models here.
#registra el modelo creado en el admin
#sitio de la pagina admin registre la clase del modelo

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','descripcion','precio')
    ordering = ('title','precio')
    search_fields = ('title','precio','descripcion')
    list_filter = ('title','precio')
    readonly_fields = ('created','updated')


admin.site.register(project,ProjectAdmin)
    




