# module_human_resources/views.py
from ceta.module_generic.views import AllowedGeneralView, GeneralView
from .serializers import *
from .models import *

class CategoryViewSet(AllowedGeneralView):
    serializer_class = CategorySerializer
    model = Category
    def get_queryset(self):        
        return Category.objects.filter(is_active = True)


class EmployeeViewSet(AllowedGeneralView):
    model = Employee
    serializer_class = EmployeeSerializer