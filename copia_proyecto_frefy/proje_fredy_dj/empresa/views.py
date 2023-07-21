from django.shortcuts import render,redirect
from .models import empresa
from core.models import redes
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required (login_url='/admin/login/')
def variable(request):
    empresas=empresa.objects.all()
    linkmedia=redes.objects.all() 
    return render(request,"empresa/empresa.html",{'empresas':empresas,'linkmedia': linkmedia})

