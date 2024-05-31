# module_reports/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from ceta.module_contract.models import Contract

class Clients_ContractReportsSerializers(serializers.ModelSerializer):
       
    class Meta:
        model = Contract
        fields = ['title_ct',
                 'manager_ct',
                 'start_ct',
                 'end_ct',
                 'work_area_ct',
                 'currency_ct'
                 'net_income']
