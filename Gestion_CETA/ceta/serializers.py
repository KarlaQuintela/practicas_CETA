from rest_framework import fields 
from rest_framework_json_api import serializers

from .exceptions import *
from .models import *
from ceta.module_accounting.models import *
from ceta.module_contract.models import *
from ceta.module_human_resources.models import *
from ceta.module_offer.models import *
from ceta.module_user.models import *


# module_human_resources
class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Category
        fields = ('name_cg', 'hourly_wage_cg')

class EmployeeSerializer(serializers.ModelSerializer):
    fk_id_cg = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many=False)
    
    class Meta:
        model = Employee
        fields = (
            'id_em',
            'fk_id_cg', 
            'name_em',
            'address_em',
            'phone_em',
            'email_em',
            'department_em',
            'num_account_em'         
        )

    """
    def validate(self, res: OrderedDict):
        category = res.get("category")
        if not category.functionvalidation():
            raise CategoryNotFoundException
        return res
    """

        
