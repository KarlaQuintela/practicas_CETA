from ceta.module_offer.views import *
def parameter_list():
    return [
        (r'training', TrainingViewSet, 'training'),
        (r'service', ServiceViewSet, 'service')
    ]

