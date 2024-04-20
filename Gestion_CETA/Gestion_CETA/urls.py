from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('ceta/', include('ceta.urls')),  # Ruta principal de la aplicación 
]
 