from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .module_human_resources.views import *
from ceta.module_contract.views import *
from ceta.module_offer.views import *
from ceta.module_accounting.views import *

router = routers.DefaultRouter()

# module_human_resources
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'employee', EmployeeViewSet, basename='employee')

# module_contract
router.register(r'client', ClientViewSet, basename='client')
router.register(r'contract', ContractViewSet, basename='contract')
router.register(r'payterm', PaymentTermViewSet, basename='payterm')
router.register(r'payemployee', PaymentEmployeeViewSet, basename='payemployee')

# module_offer
router.register(r'training', TrainingViewSet, basename='training')
router.register(r'service', ServiceViewSet, basename='service')

# module_accounting
router.register(r'bill', BillViewSet, basename='bill')
router.register(r'receipt', ReceiptViewSet, basename='receipt')
router.register(r'remuneration', RemunerationViewSet, basename='remuneration')

urlpatterns = router.urls
urlpatterns +=[     
    path('api-token-auth/', obtain_auth_token), #access to token auth    
]