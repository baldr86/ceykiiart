from django.shortcuts import render
from .forms import userEditForm, UserRegisterForm, AvatarFormulario
from .models import FanArt, OriginalWork, Avatar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request): #CAMBIAR

        imagenes = FanArt.objects.all() #cambiar por una pagina de presentacion

        return render(request, "ilustration.html", {'imagenes': imagenes})

def fanArt(request):

        imagenes = FanArt.objects.all()

        return render(request, "fanart.html", {'imagenes': imagenes})

def originalWork(request):

        imagenes = OriginalWork.objects.all() 

        return render(request, "originalwork.html", {'imagenes': imagenes})


#views de usuario
def crearUser(request):
    if request.method == "POST":

        form = UserRegisterForm (request.POST)
        if form.is_valid():

            username= form.cleaned_data['username']
            form.save()           
            return render (request, 'index.html', {'mensaje': 'Usuario Creado con éxito :) '})
           
        else:
            return render (request, 'index.html', {'mensaje': 'Usuario no creado, intenta nuevamente'})

    else:
        form = UserRegisterForm ()
        return render (request, 'crearcuenta.html', {'form': form})        

@login_required
def perfil(request):
        avatares = Avatar.objects.filter(user=request.user.id) 
        fotoPerfil = []
        for avatar in avatares:
                fotoPerfil.append(avatar)
        
        if not fotoPerfil:
                pass
        
        else:
                ultimaImagen = fotoPerfil.pop()
                

        if not avatares:
                return render(request, 'perfil.html', {'url': '/media/avatar/avatar.png'})
        else:
                print(ultimaImagen)
                return render(request, 'perfil.html', {'url': ultimaImagen.imagen.url})
 

@login_required
def editarPerfil(request):
        user = request.user

        if request.method == "POST":
                myForm = userEditForm(request.POST)
                if myForm.is_valid():
                        info = myForm.cleaned_data
                        user.username = info["username"]
                        user.email = info["email"]
                        user.password1 = info["password1"]
                        user.password2 = info["password2"]
                        user.save()

                        return render(request, "perfil.html")
        else:
                myForm = userEditForm(initial={"email" : user.email})
        
        return render(request, "editarperfil.html", {"myForm" : myForm, "user" : user})

@login_required
def avatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES)

            if miFormulario.is_valid(): 


                  u = User.objects.get(username=request.user)
                  
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "inicio.html") 
      else: 

            miFormulario= AvatarFormulario()

      return render(request, "agregaravatar.html", {"miFormulario":miFormulario})
