# module_human_resources/models.py
from django.db import models

class Category(models.Model):
    id_cg = models.AutoField(primary_key=True)
    name_cg = models.CharField(max_length=255)
    hourly_wage_cg = models.FloatField()

    def __str__(self):
        return f"{self.name_cg}, {self.hourly_wage_cg}"

class Worker(models.Model):
    id_w = models.CharField(max_length=11, primary_key=True)
    fk_id_cg = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_w = models.CharField(max_length=255)
    address_w = models.CharField(max_length=255)
    phone_w = models.CharField(max_length=255)
    email_w = models.CharField(max_length=255)
    department_w = models.CharField(max_length=255)
    num_account_w = models.CharField(max_length=16)

    def __str__(self):
        return self.name_w
