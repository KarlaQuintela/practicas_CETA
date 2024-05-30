# module_offer/views.py

from ceta.module_generic.views import AllowedGeneralView
from .serializers import *
from .models import *

class TrainingViewSet(AllowedGeneralView):
    model = Training
    serializer_class = TrainingSerializer
class ServiceViewSet(AllowedGeneralView):
    model = Service
    serializer_class = ServiceSerializer