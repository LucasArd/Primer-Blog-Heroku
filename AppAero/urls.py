from django.urls import path
from AppAero import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler404



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pasajerosformulario', views.PasajerosFormulario, name='pasajerosformulario'),
    path('azafatasformulario', views.AzafatasFormulario, name='azafatasformulario'),
    path('administrativosformulario', views.AdministrativosFormulario, name='administrativosformulario'),
    path('pilotosformulario', views.PilotosFormulario, name = 'pilotosformulario'),
#---------------------------------------------------------------------------------------------
    path('buscar/', views.Buscar, name = 'buscar'),
    path('busquedaapellido', views.BusquedaApellido, name = 'busquedaapellido'),
#----------------------------------------------------------------------------------------------
    path('pasajeros', views.PasajerosList.as_view(), name = 'pasajeros'),
    path('pasajeros/list', views.PasajerosList.as_view(), name = 'pasajeroslist'),
    path('pasajeros/<pk>', views.PasajerosDetail.as_view(), name = 'pasajerosdetail'),
    path('pasajeros/nuevo/', views.PasajerosCreate.as_view(), name = 'pasajeroscreate'),
    path('pasajeros/edicion/<pk>', views.PasajerosUpdate.as_view(), name = 'pasajerosupdate'),
    path('pasajeros/borrar/<pk>', views.PasajerosDelete.as_view(), name = 'pasajerosdelete'),
#----------------------------------------------------------------------------------------------
    path('azafatas', views.AzafatasList.as_view(), name = 'azafatas'),
    path('azafatas/list', views.AzafatasList.as_view(), name = 'azafataslist'),
    path('azafatas/<pk>', views.AzafatasDetail.as_view(), name = 'azafatasdetail'),
    path('azafatas/nuevo/', views.AzafatasCreate.as_view(), name = 'azafatascreate'),
    path('azafatas/edicion/<pk>', views.AzafatasUpdate.as_view(), name = 'azafatasupdate'),
    path('azafatas/borrar/<pk>', views.AzafatasDelete.as_view(), name = 'azafatasdelete'),
#----------------------------------------------------------------------------------------------- 
    path('pilotos', views.PilotosList.as_view(), name = 'pilotos'),
    path('pilotos/list', views.PilotosList.as_view(), name = 'pilotoslist'),
    path('pilotos/<pk>', views.PilotosDetail.as_view(), name = 'pilotosdetail'),
    path('pilotos/nuevo/', views.PilotosCreate.as_view(), name = 'pilotoscreate'),
    path('pilotos/edicion/<pk>', views.PilotosUpdate.as_view(), name = 'pilotosupdate'),
    path('pilotos/borrar/<pk>', views.PilotosDelete.as_view(), name = 'pilotosdelete'),
#----------------------------------------------------------------------------------------------- 
    path('administrativos', views.AdministrativosList.as_view(), name = 'administrativos'),
    path('administrativos/list', views.AdministrativosList.as_view(), name = 'administrativoslist'),
    path('administrativos/<pk>', views.AdministrativossDetail.as_view(), name = 'administrativosdetail'),
    path('administrativos/nuevo/', views.AdministrativosCreate.as_view(), name = 'administrativoscreate'),
    path('administrativos/edicion/<pk>', views.AdministrativosUpdate.as_view(), name = 'administrativosupdate'),
    path('administrativos/borrar/<pk>', views.AdministrativosDelete.as_view(), name = 'administrativosdelete'),
#----------------------------------------------------------------------------------------------- 
    path('login', views.login_request, name = 'login'),
    path('register', views.register_request, name = 'register'),
    path('logout', LogoutView.as_view(template_name = 'AppAero/logout.html'), name = 'logout'),

    path('editarperfil', views.editarPerfil, name = 'editarperfil'),
#----------------------------------------------------------------------------------------------
    path('about', views.about, name = 'about'),
]