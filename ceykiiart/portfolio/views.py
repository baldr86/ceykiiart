from django.shortcuts import render

from .models import FanArt, OriginalWork

def index(request):

        imagenes = FanArt.objects.all() #cambiar por una pagina de presentacion

        return render(request, "ilustration.html", {'imagenes': imagenes})

def fanArt(request):

        imagenes = FanArt.objects.all()

        return render(request, "fanart.html", {'imagenes': imagenes})

def originalWork(request):

        imagenes = OriginalWork.objects.all() 

        return render(request, "originalwork.html", {'imagenes': imagenes})