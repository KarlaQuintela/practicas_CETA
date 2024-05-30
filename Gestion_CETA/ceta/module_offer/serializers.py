# module_offer/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from collections import OrderedDict
from datetime import timedelta
from ceta.validations import *
from .models import *
from ceta.module_contract.models import Contract

class TrainingSerializer(serializers.ModelSerializer):  
    fk_id_ct = serializers.PrimaryKeyRelatedField(queryset = Contract.objects.all(), many=False)
  
    class Meta:
        model = Training
        fields = '__all__'
        read_only_fields = ('is_active', 'id_tr')

    def validate(self, res: OrderedDict):
        contract = res.get('fk_id_ct')
        training_tr = res.get('training_tr')
        hours_tr =res.get('hours_tr')
        capacity_tr =res.get('capacity_tr')
        start_tr = res.get('start_tr')
        end_tr = res.get('end_tr')        
        
        # Validate contract
        if not contract.is_in_force:
            raise serializers.ValidationError({
                'fk_id_ct': 'The contract related to is not in force.'
            })

        # Validate training_tr
        if not is_valid_alpha(training_tr):
            raise serializers.ValidationError({
                'training_tr': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_characters_count(training_tr, 3):
            raise serializers.ValidationError({
                'training_tr': 'This field should contain more than 3 characters.'
            })

        # Validate hours_tr
        if hours_tr <= 0:
            raise serializers.ValidationError({
                'hours_tr': 'This field should be greater than 0.'
            })
        if hours_tr > ((end_tr - start_tr).days * 24):
            raise serializers.ValidationError({
                'hours_tr': 'Hours must not exceed the amount of hours between the start and end date.'
            })

        # Validate capacity_tr
        if capacity_tr <= 0:
            raise serializers.ValidationError({
                'capacity_tr': 'This field should be greater than 0.'
            })
        
        # Validate start_tr
        if start_tr < contract.start_ct:
            raise serializers.ValidationError({
                'start_tr': 'Start date must be later than the contract start date.'
            })
        
        # Validate end_tr
        if end_tr > contract.end_ct:
            raise serializers.ValidationError({
                'end_tr': 'End date must be before the contract end date.'
            })
        if end_tr <= start_tr:
            raise serializers.ValidationError({
                'end_tr': 'End date must be later than the start date.'
            })        
        
        return res

class ServiceSerializer(serializers.ModelSerializer):
    fk_id_ct = serializers.PrimaryKeyRelatedField(queryset = Contract.objects.all(), many=False)
    duration_serv = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = '__all__'      
        read_only_fields = ('is_active', 'id_serv') 

    def get_duration_serv(self, obj):
        return obj.duration_serv     
    
    def validate(self, res: OrderedDict):
        contract = res.get('fk_id_ct')
        product_serv = res.get('product_serv')

        # Validate contract
        if not contract.is_in_force:
            raise serializers.ValidationError({
                'fk_id_ct': 'The contract related to is not in force.'
            })

        # Validate product_serv
        if not is_valid_alpha(product_serv):
            raise serializers.ValidationError({
                'product_serv': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_characters_count(product_serv, 3):
            raise serializers.ValidationError({
                'product_serv': 'This field should contain more than 3 characters.'
            })

        return res
