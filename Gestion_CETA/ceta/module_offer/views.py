# module_offer/views.py

from ceta.module_generic.views import GeneralView, LogicDelete
from .serializers import *
from .models import *

class TrainingViewSet(GeneralView, LogicDelete):
    model = Training
    serializer_class = TrainingSerializer
class ServiceViewSet(GeneralView, LogicDelete):
    model = Service
    serializer_class = ServiceSerializer