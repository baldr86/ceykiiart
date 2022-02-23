from django.contrib import admin
from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name = "index"),
    
    #TRABAJO
    path('fanart/', views.fanArt, name = "fan art"),
    path('originalwork/', views.originalWork, name = "original work"),

    #PERFIL
    path('perfil/', views.perfil, name ="perfil"),
    path('crearperfil/', views.crearUser, name = "crear perfil"),
    path('editarperfil/', views.editarPerfil, name = "editar perfil")

    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)