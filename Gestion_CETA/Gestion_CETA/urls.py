from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
  
    path('ceta/', include('ceta.urls')),  # Ruta principal de la aplicación 
    path('ceta/module_accounting/', include('ceta.module_accounting.urls')),  # Módulo contabilidad
    path('ceta/module_contract/', include('ceta.module_contract.urls')),  # Módulo de cliente-contrato
    path('ceta/module_human_resources/', include('ceta.module_human_resources.urls')),  # Módulo de recursos humanos
    path('ceta/module_offer/', include('ceta.module_offer.urls')),  # Módulo de oferta    
    path('ceta/module_user/', include('ceta.module_user.urls')),  # Módulo de usuarios
]
