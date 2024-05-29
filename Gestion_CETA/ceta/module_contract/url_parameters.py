from ceta.module_contract.views import *
def parameter_list():
    return [
        (r'client', ClientViewSet, 'client'),
        (r'contract', ContractViewSet, 'contract'),
        (r'payterm', PaymentTermViewSet, 'payterm'),
        (r'payemployee', PaymentEmployeeViewSet, 'payemployee')
    ]
    