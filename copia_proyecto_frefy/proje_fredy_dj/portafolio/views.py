from django.shortcuts import render
from .models import project
from core.models import redes

# Create your views here.
def portafolio(request):
    projects=project.objects.all() 
    linkmedia=redes.objects.all() 
#variable es igual a la clase, objects para traer todos los objectos de la clase project
    return render(request,"portafolio/portafolio.html",{'projects':projects,'linkmedia': linkmedia}) #render(renderizar) #nombre que le voy a pasar a ese nuevo objecto

def productos(request):
    prod=project.objects.all()
    linkmedia = redes.objects.all()
    return render(request,"portafolio/productos.html",{'prod':prod,'linkmedia':linkmedia})