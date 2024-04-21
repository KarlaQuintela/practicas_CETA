# module_offer/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from Gestion_CETA.utils import validations
from .models import *
from ceta.module_contract.models import Contract

class TrainingSerializer(serializers.ModelSerializer):  
    fk_id_ct = serializers.PrimaryKeyRelatedField(queryset = Contract.objects.all(), many=False)
  
    class Meta:
        model = Training
        fields = '__all__'
        read_only_fields = ('is_active', 'id_tr')

class ServiceSerializer(serializers.ModelSerializer):
    fk_id_ct = serializers.PrimaryKeyRelatedField(queryset = Contract.objects.all(), many=False)
    
    class Meta:
        model = Service
        fields = '__all__'      
        read_only_fields = ('is_active', 'id_serv')      
    