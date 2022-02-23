
from tkinter.font import BOLD
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#Formularios de carga de trabajos
class fanArtForm(forms.Form):   
    titulo = forms.CharField()
    imagen = forms.ImageField()

class originalWorkForm(forms.Form):   
    titulo = forms.CharField()
    imagen = forms.ImageField()
    

#Formularios de usuario
class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    imagen_avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name', 'last_name', 'imagen_avatar'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class userEditForm(UserCreationForm):
    username =forms.CharField()
    email = forms.EmailField(label= "modificar correo electronico")
    password1 = forms.CharField(label="contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="repetir contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField(required=True)