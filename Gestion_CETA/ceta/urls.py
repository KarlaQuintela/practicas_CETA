from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

import ceta.module_human_resources.url_parameters  as human_resources
import ceta.module_contract.url_parameters as contract
import ceta.module_offer.url_parameters as offer
import ceta.module_accounting.url_parameters as accounting
import ceta.module_reports.url_parameters as reports
from .views import pdfExport

router = routers.DefaultRouter()
router.register
modules = [human_resources,contract,offer,accounting,reports]
for route in modules:
    for parameters in route.parameter_list():
        prefix,viewset,basename = parameters
        router.register(prefix,viewset,basename=basename)


urlpatterns = router.urls
urlpatterns +=[     
    path('api-token-auth/', obtain_auth_token), #access to token auth 
    path('pdf', pdfExport, name="pdfExport"),    
]
