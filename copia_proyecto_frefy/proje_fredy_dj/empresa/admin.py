from django.contrib import admin
from .models import empresa
# Register your models here.

class mision_visionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
admin.site.register(empresa, mision_visionAdmin)