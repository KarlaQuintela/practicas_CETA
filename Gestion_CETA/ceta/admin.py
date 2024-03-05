from django.contrib import admin
from ceta.module_accounting.models import *
from ceta.module_contract.models import *
from ceta.module_human_resources.models import *
from ceta.module_offer.models import *
from ceta.module_user.models import *

# Register your models here.
admin.site.register(Bill)
admin.site.register(Receipt)
admin.site.register(Remuneration)

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(PaymentTerm)
admin.site.register(PaymentWorker)
admin.site.register(Expense)

admin.site.register(Category)
admin.site.register(Worker)

admin.site.register(User)
admin.site.register(Role)
