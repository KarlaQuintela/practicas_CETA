from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .module_human_resources.views import *

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns +=[     
    path('api-token-auth/', obtain_auth_token), #access to token auth    
]