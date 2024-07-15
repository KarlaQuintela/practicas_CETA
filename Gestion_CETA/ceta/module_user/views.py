# module_user/views.py

import json
from ceta.module_generic.views import AllowedGeneralView, GeneralView
from rest_framework.mixins import DestroyModelMixin
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import *


from .models import User, Role


class UserViewSet(AllowedGeneralView, DestroyModelMixin):
    model = User
    serializer_class = UserSerializer
class RoleViewSet(AllowedGeneralView, DestroyModelMixin):
    model = Role
    serializer_class = RoleSerializer


@api_view(['POST'])
def create_user(request):
    data = request.data
    #validate
    return Response(data=data,status=HTTP_200_OK)