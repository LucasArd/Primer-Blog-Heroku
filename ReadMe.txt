- La página principal es:
http://127.0.0.1:8000/AppAero/

- En el header están las cuatro opciones que llevan a las distintas clases (pasajeros, azafatas, pilotos y boletos), y
también la función de busqueda.

- Haciendo click en las primeras cuatro opciones mencionadas lleva al usuario a un formulario donde puede insertar
datos de un nuevo objeto que pertenezca al modelo seleccionado.

- Haciendo click en el botón "Busqueda", el usuario puede ingresar el apellido de la persona que busca. El sistema
muestra todos los pasajeros, pilotos y/o azafatas con ese apellido.

#----------------------------------------------------------------------------------------------------------------------

- Creamos CRUD por Vista de:
pasajeros, azafatas y pilotos

- Modificando Settings.py a:
DEBUG = False
ALLOWED_HOSTS = ["*"]

- Agregamos ruta de STATIC para que pueda obtener los archivos de STATIC ya que si no hacemos esto la pagina carga sin static files
STATICFILES_DIRS = [
    BASE_DIR / "C:/Users/luqas/Desktop/ProyectoFinalClone/Primer-Blog/AppAero/static", 
]

- Creamos vista, url y template ABOUT/ en donde hablamos de nosotros los desarrolladores. Ademas agregamos boton de redireccionamiento

- Cambiamos el Model BOLETO por PERSONAL ADMINISTRATIVO, para darle mas sentido a la pagina. Esto conlleva la modificacion de las views, urls, base de datos, formularios, etc.

- Se crea  INICIO con direccionammiento directo desde localhost, aunque tambien se deja INICIO desde AppAero/INICIO. 