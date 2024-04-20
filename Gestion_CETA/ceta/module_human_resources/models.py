# module_human_resources/models.py
from django.db import models

class Category(models.Model):
    id_cg = models.AutoField(primary_key=True)
    name_cg = models.CharField(max_length=15, unique=True)
    hourly_wage_cg = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name_cg}"

class Employee(models.Model):
    id_em = models.CharField(max_length=11, primary_key=True)
    fk_id_cg = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_em = models.CharField(max_length=50, unique=True) 
    address_em = models.CharField(max_length=255)
    phone_em = models.CharField(max_length=15)
    email_em = models.EmailField(verbose_name="Email", unique=True)
    department_em = models.CharField(max_length=255)
    num_account_em = models.CharField(max_length=16, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name_em}, {self.id_em}"
