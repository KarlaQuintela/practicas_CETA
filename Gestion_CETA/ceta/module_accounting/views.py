# module_accounting/views.py
from ceta.module_generic.views import GeneralView
from .serializers import *
from .models import *

class BillViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

class ReceiptViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Receipt
    serializer_class = ReceiptSerializer

class RemunerationViewSet(GeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Remuneration
    serializer_class = RemunerationSerializer