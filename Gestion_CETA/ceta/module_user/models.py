# module_user/models.py
from django.contrib.auth.models import User,Group
class User(User):    
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

class Role(Group):
    
    def __str__(self):
        return self.name_role
