# module_accounting/views.py
from json import JSONDecodeError
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
 
from .serializers import *
from .models import *

class BillViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'pk'

class ReceiptViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    lookup_field = 'pk'

class RemunerationViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet      
        ):
    #permission_classes = (IsAuthenticated,)
    queryset = Remuneration.objects.all()
    serializer_class = RemunerationSerializer
    lookup_field = 'pk'