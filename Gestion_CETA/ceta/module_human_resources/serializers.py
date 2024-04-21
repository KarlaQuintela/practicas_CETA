# module_human_resources/serializers.py
from rest_framework import fields 
from rest_framework_json_api import serializers

from ceta.exceptions import *
from .models import *

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('is_active', 'id_cg')

class EmployeeSerializer(serializers.ModelSerializer):
    fk_id_cg = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many=False)
    
    class Meta:
        model = Employee
        fields = '__all__'      
        read_only_fields = ('is_active')

    """
    def validate(self, res: OrderedDict):
        category = res.get("category")
        if not category.functionvalidation():
            raise CategoryNotFoundException
        return res
    """

        
