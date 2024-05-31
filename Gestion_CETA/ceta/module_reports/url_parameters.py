from .views import *

def parameter_list():
    return [
        (r'clients_contract', ReportsViewset, 'clients_contract'),        
    ]
    