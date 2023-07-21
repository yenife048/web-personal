from django.contrib import admin
from .models import redes, category, post

# Register your models here.
#class redAdmin(admin.ModelAdmin):
    #readonly_fields=('created','updated')

class redesAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class categoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class postAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(redes,redesAdmin)
admin.site.register(category,categoryAdmin)
admin.site.register(post,postAdmin)