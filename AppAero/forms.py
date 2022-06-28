
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Pilotosformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    horasDeVuelo = forms.IntegerField()

class Pasajerosformulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    
class Administrativosformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    legajo = forms.IntegerField()

class Azafatasformulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    legajo = forms.IntegerField()

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username" , "email" , "password1" , "password2"]
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(max_length=40)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Modificar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget=forms.PasswordInput)

    #last_name = forms.CharField(label='Modificar el apellido')
    #first_name = forms.CharField(label='Modificar el nombre')

    class Meta:
        model = User
        fields = ["username" , "email" , "password1" , "password2"]
        help_text = {k:"" for k in fields}
