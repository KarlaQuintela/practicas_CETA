# module_accounting/views.py
from ceta.module_generic.views import AllowedGeneralView
from .serializers import *
from .models import *

class BillViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    serializer_class = BillSerializer

class ReceiptViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Receipt
    serializer_class = ReceiptSerializer

class RemunerationViewSet(AllowedGeneralView):
    #permission_classes = (IsAuthenticated,)
    model = Remuneration
    serializer_class = RemunerationSerializer