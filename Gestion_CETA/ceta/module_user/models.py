# module_user/models.py
from django.db import models
from django.contrib.auth import models
class User(models.User):
    fk_id_role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=255)
    description_role = models.TextField()    

    def __str__(self):
        return self.name_role
