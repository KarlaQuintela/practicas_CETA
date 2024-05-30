# module_accounting/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from ceta.validations import *
from .models import *
from ceta.module_contract.models import PaymentTerm

class BillSerializer(serializers.ModelSerializer):  
    fk_id_payterm = serializers.PrimaryKeyRelatedField(queryset = PaymentTerm.objects.all(), many=False)
  
    class Meta:
        model = Bill
        fields = '__all__'
        read_only_fields = ('id_bill',)

class ReceiptSerializer(serializers.ModelSerializer):  
    fk_id_bill = serializers.PrimaryKeyRelatedField(queryset = Bill.objects.all(), many=False)
  
    class Meta:
        model = Receipt
        fields = '__all__'
        read_only_fields = ('id_rec',)

class RemunerationSerializer(serializers.ModelSerializer):  
    fk_id_bill = serializers.PrimaryKeyRelatedField(queryset = Bill.objects.all(), many=False)
  
    class Meta:
        model = Remuneration
        fields = '__all__'
        read_only_fields = ('id_rem',)