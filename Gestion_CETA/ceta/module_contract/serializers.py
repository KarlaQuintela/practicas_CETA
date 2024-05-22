# module_contract/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from datetime import timedelta
from ceta import validations
from .models import *
from ceta.module_human_resources.models import Employee

class ClientSerializer(serializers.ModelSerializer):  
 
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ('id_client')

    def validate(self, res: OrderedDict):
        name_client = res.get('name_client')  
        address_client = res.get('address_client')  
        phone_client = res.get('phone_client')  
        email_client = res.get('email_client')
        
        # Validate name_client
        if not is_valid_alpha(name_client):
            raise serializers.ValidationError({
                'name_client': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_characters_count(name_client, 3):
            raise serializers.ValidationError({
                'name_client': 'This field should contain more than 3 characters.'
            })
            
        # Validate address_client
        if not is_empty(address_client):
            if not is_valid_characters_count(address_client, 5):
                raise serializers.ValidationError({
                    'address_client': 'This field should contain more than 5 characters.'
                })
            if is_valid_address(address_client):
                raise serializers.ValidationError({
                    'address_client': 'This field should not contain special characters except for ,./#'
                })

        # Validate phone_client            
            if not is_valid_characters_count(phone_client, 10):
                raise serializers.ValidationError({
                    'phone_client': 'This field should contain more than 10 characters.'
                })
            if is_valid_phone(phone_client):
                raise serializers.ValidationError({
                    'phone_client': 'This field is not a valid phone number'
                }) 
            
        # Validate email_client
        if  email_client == null or is_empty(email_client):
            raise serializers.ValidationError({
                'email_client': 'This field is required.'
            })

        return res   

class ContractSerializer(serializers.ModelSerializer):  
    manager_ct = serializers.PrimaryKeyRelatedField(queryset = Employee.objects.all(), many=False)
    fk_id_client = serializers.PrimaryKeyRelatedField(queryset = Client.objects.all(), many=False)

    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = ('id_ct', 'is_in_force')
    
    def validate(self, res: OrderedDict):   
        manager = res.get('manager_ct')     
        title_ct = res.get('title_ct') 
        work_area_ct = res.get('work_area_ct')  
        start_ct = res.get('start_ct')
        end_ct = res.get('end_ct')
        resolution_ct = res.get('resolution_ct')   
        profit_margin = res.get('profit_margin')

        # Validate manager
        if not manager.is_active:
            raise serializers.ValidationError({
                'manager_ct': 'The employee related to is not currently active.'
            })

        # Validate title_ct        
        if not is_valid_contract_title(title_ct):    
            raise serializers.ValidationError({
                'title_ct': 'This field is not a valid contract title.'
            })
        if not is_valid_string_field(title_ct):
            raise serializers.ValidationError({
                'title_ct': 'This field should contain more than 3 characters.'
            })

        # Validate work_area_ct
        if not is_valid_alpha(work_area_ct):
            raise serializers.ValidationError({
                'work_area_ct': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_string_field(work_area_ct):
            raise serializers.ValidationError({
                'work_area_ct': 'This field should contain more than 3 characters.'
            }) 

        # Validate start_ct
        if start_ct < resolution_ct:
            raise ValidationError({
                'start_ct': 'Start date must be later than the resolution date.'
            })
        
        # Validate end_ct        
        if end_ct <= start_ct:
            raise ValidationError({
                'end_ct': 'End date must be later than the start date.'
            })

        # Validate resolution_ct
        if resolution_ct > datetime.now():
            raise ValidationError({
                'resolution_ct': 'The resolution date must be before the current date.'
            })

        # Validate profit_margin
        if profit_margin <= 0 or profit_margin >= 100:
            raise serializers.ValidationError({
                'profit_margin': 'This field should be greater than 0 and less than 100.'
            })
        
        return res  


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
