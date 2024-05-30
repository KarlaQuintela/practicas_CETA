# module_offer/views.py

from ceta.module_generic.views import AllowedGeneralView, LogicDelete
from .serializers import *
from .models import *
class TrainingViewSet(AllowedGeneralView, LogicDelete):
    model = Training
    serializer_class = TrainingSerializer
class ServiceViewSet(AllowedGeneralView, LogicDelete):
    model = Service
    serializer_class = ServiceSerializer