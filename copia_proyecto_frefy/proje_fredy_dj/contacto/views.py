from django.shortcuts import render,redirect
from core.models import redes
from.forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage #importar para lo de gmail


# Create your views here.
def contacto(request):
    
    
    contact_form=ContactForm()#se instancia para enviarlo en un diccionario
    if request.method == "POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            
            email=EmailMessage(
                "La cafetera: Nuevo Mensaje",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                
                "sandbox.smtp.mailtrap.io",
                ["yenniferadrada@gmail.com","yenyadrada@misena.edu.co"],
                reply_to=[email]
            ) 
            try:#excepcion
                email.send()
                #mensaje de envio en el caso que todo este bien
                return redirect(reverse('contacto')+"?ok")
            except:
                #error que direcciona a fail
                return redirect(reverse('contacto')+"?fail")
                   
        #return redirect(reverse('contacto')+"?Enviado Correctamente")
    linkmedia = redes.objects.all()
    return render(request, "contacto/contacto.html",{'linkmedia':linkmedia,'form':contact_form})