# module_contract/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from datetime import timedelta
from Gestion_CETA.utils import validations
from .models import *
from ceta.module_human_resources.models import Employee

class ClientSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id_client')

class ContractSerializer(serializers.ModelSerializer):  
    manager_ct = serializers.PrimaryKeyRelatedField(queryset = Employee.objects.all(), many=False)
    fk_id_client = serializers.PrimaryKeyRelatedField(queryset = Client.objects.all(), many=False)

    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ('id_ct', 'is_in_force')

class PaymentTermSerializer(serializers.ModelSerializer):  
    fk_id_ct = serializers.PrimaryKeyRelatedField(queryset = Contract.objects.all(), many=False)
  
    class Meta:
        model = PaymentTerm
        fields = '__all__'
        read_only_fields = ('id_payterm', 'is_billed')

class PaymentEmployeeSerializer(serializers.ModelSerializer):  
    fk_id_payterm = serializers.PrimaryKeyRelatedField(queryset = PaymentTerm.objects.all(), many=False)
    fk_id_em = serializers.PrimaryKeyRelatedField(queryset = Employee.objects.all(), many=False)

    class Meta:
        model = PaymentEmployee
        fields = '__all__'
        read_only_fields = ('id_pay')
