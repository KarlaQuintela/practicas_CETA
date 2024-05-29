# module_contract/views.py

from ceta.module_generic.views import GeneralView
from .serializers import *
from .models import *

class ClientViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Client
    serializer_class = ClientSerializer

class ContractViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Contract
    serializer_class = ContractSerializer

class PaymentTermViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = PaymentTerm
    serializer_class = PaymentTermSerializer

class PaymentEmployeeViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = PaymentEmployee
    serializer_class = PaymentEmployeeSerializer
