# module_user/views.py

from ceta.module_generic.views import AllowedGeneralView, GeneralView
from rest_framework.mixins import DestroyModelMixin
from .serializers import *
from .models import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from serializers import UserSerializer,RoleSerializer

from django.shortcuts import render, redirect,get_object_or_404

from .models import User, Role

from ceta.email_sender import send_mail

@api_view(['GET'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])
    response = Response({})
    if not user.check_password(request.data['password']):
        response = Response({'error': 'invalid password'},status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user)
        serialized_user = UserSerializer(instance=user)
        response = Response({
            'token': token.key, 
            "user": serialized_user.data
        },status=status.HTTP_200_OK)
    return response
@api_view(['POST'])
def sign_in(request):
    #TODO add role
    # role = Role.objects.filter(name_role=request.data.role).get('id_role')
    # request_data: dict = {}
    user_data = UserSerializer(data=request.data)
    response = Response({user_data.errors},status=status.HTTP_400_BAD_REQUEST)
    if(user_data.is_valid()):
        user_data.save()
        user = User.objects.get(username=user_data.data['username'])
        user.set_password(user_data.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        response.data = {
        'token': token.key,
        "user": user_data.data
        }
        response.status_code = status.HTTP_201_CREATED
        send_mail(user.get_email_field_name)
    return response

class UserViewSet(AllowedGeneralView, DestroyModelMixin):
    model = User
    serializer_class = UserSerializer
class RoleViewSet(AllowedGeneralView, DestroyModelMixin):
    model = Role
    serializer_class = RoleSerializer
