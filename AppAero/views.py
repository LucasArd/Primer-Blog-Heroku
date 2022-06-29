
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pasajero, Piloto, Administrativo, Azafatas
from AppAero.forms import  Pasajerosformulario, Pilotosformulario, Administrativosformulario, Azafatasformulario, UserRegistrationForm, UserEditForm
from django.views.generic import ListView,TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import datetime


def inicio (request):
    dia = datetime.datetime.now()
    documentoDeTexto = f'{dia.date()}'

    return render(request, "AppAero/inicio.html",{'fecha':documentoDeTexto})

def PasajerosFormulario (request):
    if request.method == 'POST':

        miFormulario = Pasajerosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']

            pasajero = Pasajero(nombre = nombre, apellido= apellido)

            pasajero.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Pasajerosformulario()
    return render(request, "AppAero/pasajerosformulario.html", {"miFormulario":miFormulario})

def AzafatasFormulario (request):
    if request.method == 'POST':

        miFormulario = Azafatasformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            legajo = informacion['legajo']

            azafata = Azafatas(nombre = nombre, apellido= apellido, legajo= legajo)

            azafata.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Azafatasformulario()
    return render(request, "AppAero/azafatasformulario.html", {"miFormulario":miFormulario})

def AdministrativosFormulario (request):
    if request.method == 'POST':

        miFormulario = Administrativosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            legajo = informacion['legajo']

            administrativos = Administrativo(nombre = nombre, apellido= apellido, legajo = legajo)

            administrativos.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Administrativosformulario()
    return render(request, "AppAero/administrativosformulario.html", {"miFormulario":miFormulario})

def PilotosFormulario (request):
    if request.method == 'POST':

        miFormulario = Pilotosformulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            horasDeVuelo = informacion['horasDeVuelo']

            piloto = Piloto(nombre = nombre, apellido= apellido, horasDeVuelo = horasDeVuelo)

            piloto.save()

            return render(request, "AppAero/inicio.html")
    else:
        miFormulario = Pilotosformulario()
    return render(request, "AppAero/pilotosformulario.html", {"miFormulario":miFormulario})


def Buscar (request):
    if request.GET['apellido']:
        apellido = request.GET['apellido']
        pasajeros = Pasajero.objects.filter(apellido__icontains=apellido)
        pilotos = Piloto.objects.filter(apellido__icontains=apellido)
        azafatas = Azafatas.objects.filter(apellido__icontains=apellido)

        return render(request, "AppAero/resultadosbusqueda.html", {"apellido":apellido, "pasajeros":pasajeros, "pilotos":pilotos, "azafatas":azafatas})
    else:
        respuesta = "Los datos no fueron enviados correctamente."
    return HttpResponse(respuesta)

def BusquedaApellido (request):
    return render(request, "AppAero/busquedaapellido.html")

#------------------- PASAJEROS CRUD ------------------------------------------------

class PasajerosList(LoginRequiredMixin, ListView):
    model = Pasajero
    template_name = "AppAero/pasajeros_list.html"

class PasajerosDetail(DetailView):
    model = Pasajero
    template_name = "AppAero/pasajeros_detail.html"

class PasajerosCreate(CreateView):
    model = Pasajero
    success_url = reverse_lazy('pasajeroslist')
    fields = ['nombre', 'apellido']

class PasajerosUpdate(UpdateView):
    model = Pasajero
    success_url = reverse_lazy('pasajeroslist')
    fields = ['nombre', 'apellido']

class PasajerosDelete(DeleteView):
    model = Pasajero
    success_url = reverse_lazy('pasajeroslist')

#------------------- AZAFATAS CRUD ------------------------------------------------

class AzafatasList(LoginRequiredMixin, ListView):
    model = Azafatas
    template_name = "AppAero/azafatas_list.html"

class AzafatasDetail(DetailView):
    model = Azafatas
    template_name = "AppAero/azafatas_detail.html"

class AzafatasCreate(CreateView):
    model = Azafatas
    success_url = reverse_lazy('azafataslist')
    fields = ['nombre', 'apellido', 'legajo']

class AzafatasUpdate(UpdateView):
    model = Azafatas
    success_url = reverse_lazy('azafataslist')
    fields = ['nombre', 'apellido', 'legajo']

class AzafatasDelete(DeleteView):
    model = Azafatas
    success_url = reverse_lazy('azafataslist')

#------------------- PILOTOS CRUD ------------------------------------------------

class PilotosList(LoginRequiredMixin, ListView):
    model = Piloto
    template_name = "AppAero/pilotos_list.html"

class PilotosDetail(DetailView):
    model = Piloto
    template_name = "AppAero/pilotos_detail.html"

class PilotosCreate(CreateView):
    model = Piloto
    success_url = reverse_lazy('pilotoslist')
    fields = ['nombre', 'apellido', 'horasDeVuelo']

class PilotosUpdate(UpdateView):
    model = Piloto
    success_url = reverse_lazy('pilotoslist')
    fields = ['nombre', 'apellido', 'horasDeVuelo']

class PilotosDelete(DeleteView):
    model = Piloto
    success_url = reverse_lazy('pilotoslist')

#------------------- ADMINISTRATIVOS CRUD ------------------------------------------------

class AdministrativosList(LoginRequiredMixin, ListView):
    model = Administrativo
    template_name = "AppAero/administrativos_list.html"

class AdministrativossDetail(DetailView):
    model = Administrativo
    template_name = "AppAero/administrativos_detail.html"

class AdministrativosCreate(CreateView):
    model = Administrativo
    success_url = reverse_lazy('administrativoslist')
    fields = ['nombre', 'apellido', 'legajo']

class AdministrativosUpdate(UpdateView):
    model = Administrativo
    success_url = reverse_lazy('administrativoslist')
    fields = ['nombre', 'apellido', 'legajo']

class AdministrativosDelete(DeleteView):
    model = Administrativo
    success_url = reverse_lazy('administrativoslist')

#--------------- LOGIN

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            # Autentificacion del usuario
            user = authenticate(username = usuario, password = clave)

            if user is not None:
                login (request, user) # si existe un usuario lo loguea
                return render(request, 'AppAero/inicio.html', {'mensaje': f'Bienvenido {usuario}'})

            else: 
                return render(request,'AppAero/inicio.html',{'mensaje': 'Datos incorrectos'})

        else:
            return render(request,'AppAero/inicio.html',{'mensaje': 'Carga erronea de Login'})

    else:
        form = AuthenticationForm()
        return render(request, 'AppAero/login.html', {'form': form})

def register_request (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppAero/inicio.html", {'mensaje': f"Usuario {username} creado"})
    else:
        form = UserRegistrationForm()
    
    return render(request, "AppAero/register.html",{"form":form})
            


@login_required
def editarPerfil (request):
    # Viene del modelo de Django para usuarios
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance = usuario)
        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppAero/inicio.html",{'usuario': usuario,'mensaje':'Datos actualizados correctamente'})
    else:
        formulario = UserEditForm(instance = usuario)
    return render(request,'AppAero/editarperfil.html', {'formulario': formulario, 'usuario': usuario.username})
#--------------------------------------------------------------------------------------------------------------------

def about (request):
    return render(request,'AppAero/about.html')

def error_404_view (request,exception):
    return render(request,'404.html')
