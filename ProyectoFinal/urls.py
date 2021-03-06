

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import include
from AppAero.views import inicio



urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppAero/', include('AppAero.urls')),
    path('', inicio, name='inicio'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'AppAero.views.error_404_view'