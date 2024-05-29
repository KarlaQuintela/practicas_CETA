from ceta.module_accounting.views import *
def parameter_list():
    return [
        (r'bill', BillViewSet, 'bill'),
        (r'receipt', ReceiptViewSet, 'receipt'),
        (r'remuneration', RemunerationViewSet, 'remuneration')
    ]