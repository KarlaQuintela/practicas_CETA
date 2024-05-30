# module_user/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers
from django.core.exceptions import ValidationError
from collections import OrderedDict
from ceta.validations import *
from .models import *

class RoleSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ('id_role',)

    def validate(self, res: OrderedDict):
        name_role = res.get('name_role')         

        if not is_valid_alpha(name_role):
            raise serializers.ValidationError({
                'name_role': 'This field should contain only alphabetic characters.'
            })
        if not is_valid_characters_count(name_role, 3):
            raise serializers.ValidationError({
                'name_role': 'This field should contain more than 3 characters.'
            })
        
        return res


class UserSerializer(serializers.ModelSerializer):
    fk_id_role = serializers.PrimaryKeyRelatedField(queryset = Role.objects.all(), many=False)
     
    class Meta:
        model = User
        fields = '__all__'      
        read_only_fields = ('id_user',)

    def validate(self, res: OrderedDict):
            name_user = res.get('name_user')   
            password_user = res.get('password_user')

            # Validate name_user
            if not is_valid_alpha(name_user):
                raise serializers.ValidationError({
                    'name_user': 'This field should contain only alphabetic characters.'
                })
            if not is_valid_characters_count(name_user, 3):
                raise serializers.ValidationError({
                    'name_user': 'This field should contain more than 3 characters.'
                })
            
            #Validate password_user
            if not is_valid_characters_count(password_user, 7):
                raise serializers.ValidationError({
                    'password_user': 'This field should contain more than 7 characters.'
                })
            
            return res
        
