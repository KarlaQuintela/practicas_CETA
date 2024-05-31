# module_reports/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers as serial
from rest_framework import serializers
from ceta.module_contract.models import *
from ceta.module_accounting.models import Bill
from ceta.module_human_resources.models import Employee

class Report_Clients_ContractSerializer(serial.ModelSerializer):

    class Meta:
        model = Contract
        fields = ['title_ct',
                 'manager_ct',
                 'start_ct',
                 'end_ct',
                 'work_area_ct',
                 'currency_ct'
                 'net_income']

from rest_framework import serializers

class ReportBillSerializer(serializers.Serializer):
    id_bill = serializers.IntegerField()
    is_paid = serializers.BooleanField()
    number_payterm = serializers.IntegerField(source='fk_id_payterm.id_payterm')
    deliver_payterm = serializers.CharField(source='fk_id_payterm.deliver')
    contract = serializers.CharField(source='fk_id_payterm.fk_id_ct.title_ct')
    client = serializers.CharField(source='fk_id_payterm.fk_id_ct.fk_id_client.name_client')

    def to_representation(self, instance):
        payterm = PaymentTerm.objects.get(pk=instance.fk_id_payterm_id)
        contract = Contract.objects.get(pk=payterm.fk_id_ct_id)
        client = Client.objects.get(pk=contract.fk_id_client_id)

        data = {
            'id_bill': instance.id_bill,
            'is_paid': instance.is_paid,
            'number_payterm': payterm.id_payterm,
            'deliver_payterm': payterm.deliver,
            'contract': contract.title_ct,
            'client': client.name_client,
        }    
        return data

class ReportPendingSerializer(serializers.Serializer):
    id_bill = serializers.IntegerField()
    month_bill = serializers.IntegerField()
    number_payterm = serializers.IntegerField(source='fk_id_payterm.id_payterm')
    deliver_payterm = serializers.CharField(source='fk_id_payterm.deliver')
    contract = serializers.CharField(source='fk_id_payterm.fk_id_ct.title_ct')
    client = serializers.CharField(source='fk_id_payterm.fk_id_ct.fk_id_client.name_client')

    def to_representation(self, instance):
        payterm = PaymentTerm.objects.get(pk=instance.fk_id_payterm_id)
        contract = Contract.objects.get(pk=payterm.fk_id_ct_id)
        client = Client.objects.get(pk=contract.fk_id_client_id)

        data = {
            'id_bill': instance.id_bill,
            'month_bill': instance.month_bill,
            'number_payterm': payterm.id_payterm,
            'deliver_payterm': payterm.deliver,
            'contract': contract.title_ct,
            'client': client.name_client,
        }    
        return data

class ReportPendingDeliverySerializer(serializers.Serializer):
    id_pay = serializers.IntegerField()
    task = serializers.TextField()
    hours_pay = serializers.IntegerField()
    number_payterm = serializers.IntegerField(source='fk_id_payterm.id_payterm')
    deliver_payterm = serializers.CharField(source='fk_id_payterm.deliver')
    contract = serializers.CharField(source='fk_id_payterm.fk_id_ct.title_ct')
    employee_name = serializers.CharField(source='fk_id_em.name_em')
    employee_id = serializers.CharField(source='fk_id_em.id_em')

    def to_representation(self, instance):
        payterm = PaymentTerm.objects.get(pk=instance.fk_id_payterm_id)
        contract = Contract.objects.get(pk=payterm.fk_id_ct_id)
        employee = Employee.objects.get(pk=instance.fk_id_em_id)

        data = {
            'id_pay': instance.id_pay,
            'task': instance.task,
            'hours_pay': instance.hours_pay,
            'number_payterm': payterm.id_payterm,
            'deliver_payterm': payterm.deliver,
            'contract': contract.title_ct,
            'employee_name': employee.name_em,
            'employee_id': employee.id_em
        }    
        return data



    
