# module_offer/models.py
from django.db import models
from .module_contract.models import Contract

class Training(models.Model):
    id_tr = models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE)    
    training_tr = models.CharField(max_length=255)
    hours_tr = models.IntegerField()
    capacity_tr = models.IntegerField()
    price_tr = models.DecimalField(max_digits=10, decimal_places=2)
    start_tr = models.DateField()
    end_tr = models.DateField()

    def __str__(self):
        return self.training_tr

class Service(models.Model):
    id_serv = models.models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE)  
    product_serv = models.CharField(max_length=255)
    manager_serv = models.IntegerField()
    duration_serv = models.IntegerField()
    workers_count = models.IntegerField()
    description_serv = models.CharField(max_length=255)

    def __str__(self):
        return self.product_serv