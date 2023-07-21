from django.shortcuts import render, HttpResponse
from .models import redes

# Create your views here.

#menu para todas las paginas web

def home(request): #esperar una respuesta (request)
    linkmedia = redes.objects.all()
    return render(request, "core/home.html",{'linkmedia':linkmedia})

    
def about(request):
    linkmedia = redes.objects.all()
    return render(request, "core/about.html",{'linkmedia':linkmedia})