from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    descripcion=models.TextField(verbose_name='Descripcion')
    image=models.ImageField(verbose_name='Imagen',upload_to='projects')#upload para que las imagenes guardadas se hagan en el directorio projects
    precio=models.FloatField(verbose_name='precio', null=True)
    link=models.URLField(verbose_name="Direccion Web", null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #ordena del nuevo al antiguo
        
    def __str__(self): #cambiar el nombre del proyecto
        return self.title  # <=====
    



    