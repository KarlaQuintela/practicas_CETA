from django.contrib import admin
from django.urls import path, include
from ceta.module_user.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),  
    path('ceta/', include('ceta.urls')),  # Ruta principal de la aplicación 
    #authentication
    path('api/jwtoken/',TokenObtainPairView.as_view()),
    path('api/jwtoken/refresh',TokenRefreshView.as_view()),
]