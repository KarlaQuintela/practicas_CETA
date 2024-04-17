from .models import *
from ceta.module_accounting.models import *
from ceta.module_contract.models import *
from ceta.module_human_resources.models import *
from ceta.module_offer.models import *
from ceta.module_user.models import *

from rest_framework import fields 
from rest_framework_json_api import serializers
from .exceptions import *

# module_human_resources
class CategorySerializer(serializers.ModelSerializer):    
    name = CharField(source ="name", require=True)
    hourly_wage = FloatField(source ="hourly_wage", require=True)

    class Meta:
        model = Category
        fields = ('name', 'hourly_wage')

class Employee(serializers.ModelSerializer):
    id_em = CharField(require=True)
    category = serializers.PrimaryKeyRelatedField(queryset = Category.objects.all(), many=False)
    name = CharField(require=True)
    address = CharField(require=True)
    phone = CharField(require=True)
    email = EmailField(require=True)
    department = CharField(require=True)
    num_account = CharField(require=True)

    class Meta:
        model = Employee
        fields = (
            'id_em',
            'category', 
            'name',
            'address',
            'phone',
            'email',
            'department',
            'num_account'
        )

    """
    def validate(self, res: OrderedDict):
        category = res.get("category")
        if not category.functionvalidation():
            raise CategoryNotFoundException
        return res
    """

        
