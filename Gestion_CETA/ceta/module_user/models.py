# module_user/models.py
from django.db import models

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    fk_id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=255)
    password_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name_user

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=255)
    description_role = models.TextField()    

    def __str__(self):
        return self.name_role
