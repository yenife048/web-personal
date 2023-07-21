from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #mostrar los usuario

# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100,verbose_name='Nombre')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["created"] #ordena del nuevo al antiguo
        
    def __str__(self): #cambiar el nombre del proyecto
        return self.name #<=====

class redes(models.Model):
    title=models.CharField(max_length=50,verbose_name='Titulo')
    icon=models.CharField(max_length=50,verbose_name='Icon')
    link_redes=models.URLField(verbose_name="Direcciones Redes", null=True,blank=True)
    published = models.DateTimeField(default=now,verbose_name="Fecha de publicacion")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor") # se traen los datos de los usuarios y cuando se borran
    categorias = models.ManyToManyField(category,verbose_name="Categorias")#se trae los datos de la tabla categoria
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')
    
    class Meta:
        verbose_name = "red"
        verbose_name_plural = "redes"
        ordering = ["created"] #ordena del nuevo al antiguo
        
    def __str__(self): #cambiar el nombre del proyecto
        return self.title #<=====

class post(models.Model):
    title = models.CharField(max_length=200, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    published = models.DateTimeField(default=now,verbose_name="Fecha de publicacion")
    image = models.ImageField(upload_to='projects',null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Autor")#se tren los datos de los usuarios y cuando se borran
    categories = models.ManyToManyField(category,verbose_name="Categorias",related_name="get_posts")#se trae los datos de la tabla categorias
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha creado') #añade la hora automatica
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha Actualizado')
    
    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        
    def __str__(self): #cambiar el nombre del proyecto
        return self.title #<=====