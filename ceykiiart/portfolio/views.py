from django.shortcuts import render

from .models import Imagen


def index(request):

        imagenes = Imagen.objects.all()

        return render(request, "ilustration.html", {'imagenes': imagenes})