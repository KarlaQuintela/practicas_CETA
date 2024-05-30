# module_user/views.py
from ceta.module_generic.views import GeneralView
from rest_framework.mixins import DestroyModelMixin
from .serializers import *
from .models import *

class UserViewSet(GeneralView, DestroyModelMixin):
    model = User
    serializer_class = UserSerializer
class RoleViewSet(GeneralView, DestroyModelMixin):
    model = Role
    serializer_class = RoleSerializer