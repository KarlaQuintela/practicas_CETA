# module_offer/views.py

from ceta.module_generic.views import GeneralView
from .serializers import *
from .models import *

class TrainingViewSet(GeneralView):
    model = Training
    serializer_class = TrainingSerializer
class ServiceViewSet(GeneralView):
    model = Service
    serializer_class = ServiceSerializer