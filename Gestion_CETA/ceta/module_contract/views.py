# module_contract/views.py

from ceta.module_generic.views import AllowedGeneralView
from .serializers import *
from .models import *

class ClientViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Client
    serializer_class = ClientSerializer

class ContractViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Contract
    serializer_class = ContractSerializer

class PaymentTermViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = PaymentTerm
    serializer_class = PaymentTermSerializer

class PaymentEmployeeViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = PaymentEmployee
    serializer_class = PaymentEmployeeSerializer
