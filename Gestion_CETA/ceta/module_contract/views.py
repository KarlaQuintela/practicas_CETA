# module_contract/views.py
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
 
from .serializers import *
from .models import *

class ClientViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class ContractViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = 'pk'

class PaymentTermViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = PaymentTerm.objects.all()
    serializer_class = PaymentTermSerializer
    lookup_field = 'pk'

class PaymentEmployeeViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = PaymentEmployee.objects.all()
    serializer_class = PaymentEmployeeSerializer
    lookup_field = 'pk'
