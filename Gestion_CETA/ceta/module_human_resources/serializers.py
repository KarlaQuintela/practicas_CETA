# module_human_resources/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from django.core.exceptions import ValidationError
from collections import OrderedDict
from ceta import validations
from .models import *

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('is_active', 'id_cg')

    def validate(self, res: OrderedDict):        
        name_cg = res.get('name_cg')
        hourly_wage_cg = res.get('hourly_wage_cg')

        # Validate name_cg
        if not is_valid_alpha(name_cg):
            raise serializers.ValidationError({
                'name_cg': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_characters_count(name_cg, 3):
            raise serializers.ValidationError({
                'name_cg': 'This field should contain more than 3 characters.'
            })

        # Validate hourly_wage_cg
        if hourly_wage_cg <= 0:
            raise serializers.ValidationError({
                'hourly_wage_cg': 'This field should be greater than 0.'
            })

        return res


class EmployeeSerializer(serializers.ModelSerializer):
    fk_id_cg = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many=False)
    
    class Meta:
        model = Employee
        fields = '__all__'      
        read_only_fields = ('is_active',)

    def validate(self, res: OrderedDict):
            category = res.get('fk_id_cg') 
            id_em = res.get('id_em')        
            name_em = res.get('name_em')
            address_em = res.get('address_em')
            phone_em = res.get('phone_em')
            email_em = res.get('email_em')
            department_em = res.get('department_em')
            num_account_em = res.get('num_account_em')

            # Validate category
            if not category.is_active:
                raise serializers.ValidationError({
                    'fk_id_cg': 'The category related to is not currently active.'
                })

            # Validate id_em
            if not is_valid_id(id_em):
                raise serializers.ValidationError({
                    'id_em': 'This field should contain 11 digits and the first 6 digits should be a valid date.'
                })
            if not is_valid_age(id_em):
                raise serializers.ValidationError({
                    'id_em': 'The age related to this field can not be under 18'
                })

            # Validate name_em
            if not is_valid_alpha(name_em):
                raise serializers.ValidationError({
                    'name_em': 'This field should contain only alphabetic characters.'
                })
            if not is_valid_characters_count(name_em, 3):
                raise serializers.ValidationError({
                    'name_em': 'This field should contain more than 3 characters.'
                })
            
            # Validate address_em
            if not is_valid_characters_count(address_em, 5):
                raise serializers.ValidationError({
                    'address_em': 'This field should contain more than 5 characters.'
                })
            if is_valid_address(address_em):
                raise serializers.ValidationError({
                    'address_em': 'This field should not contain special characters except for ,./#'
                })

            # Validate phone_em
            if not is_empty(phone_em):
                if not is_valid_characters_count(phone_em, 10):
                    raise serializers.ValidationError({
                        'phone_em': 'This field should contain more than 10 characters.'
                    })
                if is_valid_phone(phone_em):
                    raise serializers.ValidationError({
                        'phone_em': 'This field is not a valid phone number'
                    }) 

            # Validate department_em
            if not is_valid_alpha(department_em):
                raise serializers.ValidationError({
                    'department_em': 'This field should contain only alphabetic characters.'
                })
            if not is_valid_characters_count(department_em, 3):
                raise serializers.ValidationError({
                    'department_em': 'This field should contain more than 3 characters.'
                })

            # Validate num_account_em           
            if not is_valid_account(num_account_em):
                raise serializers.ValidationError({
                    'num_account_em': 'This field should contain 16 digits.'
                })

            return res
        
