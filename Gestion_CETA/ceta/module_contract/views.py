# module_contract/views.py

from ceta.module_generic.views import AllowedGeneralView, LogicDelete
from .serializers import *
from .models import *
class ClientViewSet(AllowedGeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = Client
    serializer_class = ClientSerializer

class ContractViewSet(AllowedGeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = Contract
    serializer_class = ContractSerializer

class PaymentTermViewSet(AllowedGeneralView, LogicDelete):
    model = PaymentTerm

class PaymentEmployeeViewSet(AllowedGeneralView, LogicDelete):
    #permission_classes = (IsAuthenticated,)
    model = PaymentEmployee
    serializer_class = PaymentEmployeeSerializer
