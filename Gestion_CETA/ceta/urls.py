from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

import ceta.module_human_resources.url_parameters  as human_resources
import ceta.module_contract.url_parameters as contract
import ceta.module_offer.url_parameters as offer
import ceta.module_accounting.url_parameters as accounting
import ceta.module_user.url_parameters as user
from ceta.module_reports.views import ReportsViewset, generate_pdf

router = routers.DefaultRouter()
router.register
modules = [human_resources,contract,offer,accounting,user]
for route in modules:
    for parameters in route.parameter_list():
        prefix,viewset,basename = parameters
        router.register(prefix,viewset,basename=basename)


urlpatterns = router.urls
urlpatterns +=[     
    path('clients_contracts/<int:id_client>/', ReportsViewset.as_view({'get': 'clients_contracts'}), name='clients_contracts'),
    path('month_bills/<int:month>/', ReportsViewset.as_view({'get': 'month_bills'}), name='month_bills'),
    path('pending_payments/', ReportsViewset.as_view({'get': 'pending_payments'}), name='pending_payments'),
    path('pending_delivery/', ReportsViewset.as_view({'get': 'pending_delivery'}), name='pending_delivery'),

    path("pdf", generate_pdf, name="generate_pdf"),
]   
