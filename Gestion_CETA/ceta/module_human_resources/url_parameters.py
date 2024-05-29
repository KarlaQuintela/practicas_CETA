from ceta.module_human_resources.views import *
def parameter_list():
    return [
        (r'category',CategoryViewSet,'category'),
        (r'employee', EmployeeViewSet, 'employee')
    ]
    