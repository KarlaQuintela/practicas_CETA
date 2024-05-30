# module_contract/views.py

from ceta.module_generic.views import GeneralView, LogicDelete
from .serializers import *
from .models import *

class ClientViewSet(GeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = Client
    serializer_class = ClientSerializer

class ContractViewSet(GeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = Contract
    serializer_class = ContractSerializer

class PaymentTermViewSet(GeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = PaymentTerm
    serializer_class = PaymentTermSerializer

class PaymentEmployeeViewSet(GeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = PaymentEmployee
    serializer_class = PaymentEmployeeSerializer
