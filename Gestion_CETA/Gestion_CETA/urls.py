from django.contrib import admin
from django.urls import path, include
from ceta.module_user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('ceta/', include('ceta.urls')),  # Ruta principal de la aplicación 
    #authentication
    path('login',login),
    path('signin',sign_in)
]
 