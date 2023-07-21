from django.http import HttpResponse
#from django.shortcuts import redirect



def hola_mundo(request):
    return HttpResponse("Hola mundo :3")
    
    #return redirect('https://openlibra.com/es/lists/id/JgGL8V')
