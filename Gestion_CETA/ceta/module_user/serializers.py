# module_user/serializers.py
from rest_framework import fields 
from django.core.exceptions import ValidationError
from rest_framework_json_api import serializers
from collections import OrderedDict
from ceta.validations import *
from .models import *
from .serializers import *

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

