from django.db import models
from .module_contract.models import Contract
from .module_user.models import User

# Create your models here.

class Ceta(models.Model):
   id_ceta = models.AutoField(primary_key=True)
   contrats_list = models.ManyToManyField(Contract)
   users_list = models.ManyToManyField(User)
   