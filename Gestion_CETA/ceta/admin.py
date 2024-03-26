from django.contrib import admin
from .models import Ceta
from ceta.module_accounting.models import *
from ceta.module_contract.models import *
from ceta.module_human_resources.models import *
from ceta.module_offer.models import *
from ceta.module_user.models import *

# Register your models here.
admin.site.register(Ceta)

#module accounting
admin.site.register(Bill)
admin.site.register(Receipt)
admin.site.register(Remuneration)

#module contract
admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(PaymentTerm)
admin.site.register(PaymentEmployee)
admin.site.register(Expense)

#module offer
admin.site.register(Training)
admin.site.register(Service)

#module human_resources
admin.site.register(Category)
admin.site.register(Employee)

#module user
admin.site.register(User)
admin.site.register(Role)
