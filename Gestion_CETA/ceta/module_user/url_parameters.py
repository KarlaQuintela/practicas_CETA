from ceta.module_user.views import *
def parameter_list():
    return [
        (r'users',UserViewSet,'user'),
        (r'roles',RoleViewSet,'roles')
    ]