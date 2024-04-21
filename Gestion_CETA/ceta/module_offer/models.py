# module_offer/models.py
from django.db import models
from datetime import timedelta
from ceta.module_contract.models import Contract

class Training(models.Model):
    id_tr = models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE, unique=True)    
    training_tr = models.CharField(max_length=50, unique=True)
    description_tr = models.TextField(max_length=2000)
    hours_tr = models.IntegerField()
    capacity_tr = models.IntegerField()
    start_tr = models.DateField()
    end_tr = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.training_tr

class Service(models.Model):
    id_serv = models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE, unique=True)  
    product_serv = models.CharField(max_length=255)    
    description_serv = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)

    @property
    def duration_serv(self):
        return (self.fk_id_ct.end_ct - self.fk_id_ct.start_ct).days // 7

    def __str__(self):
        return self.product_serv