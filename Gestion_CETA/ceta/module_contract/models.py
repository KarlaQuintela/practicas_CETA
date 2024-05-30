# module_contract/models.py
import datetime
from django.db import models
from ceta.module_human_resources.models import Employee


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name_client = models.CharField(max_length=60, unique=True)
    address_client = models.CharField(max_length=255)
    phone_client = models.CharField(max_length=15, unique=True)
    email_client = models.EmailField(verbose_name="Email", unique=True)
    description_client = models.TextField(max_length=2000)

    def __str__(self): 
        return self.name_client

class Contract(models.Model):
    id_ct = models.AutoField(primary_key=True)
    title_ct = models.CharField(max_length=50, unique=True)
    fk_id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    manager_ct = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_ct = models.DateField()
    end_ct = models.DateField()
    resolution_ct = models.DateField()
    description_ct = models.TextField(max_length=2000)   
    work_area_ct = models.CharField(max_length=50)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2)
    currency_ct = models.CharField(max_length=10)    

    @property
    def is_in_force(self):
        in_force = True
        if self.end_ct < datetime.now():
            in_force = False
        return in_force

    @property
    def value_ct(self):
        value = PaymentTerm.objects.filter(fk_id_ct=self.id_ct).aggregate(Sum('total_amount_pay'))
        return value['total_amount_pay__sum'] or 0
    
    @property
    def net_income(self):  
        return self.value_ct + ((self.value_ct * self.profit_margin)/100)

    def __str__(self):
        return self.title_ct

class PaymentTerm(models.Model):
    id_payterm = models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE) 
    due_month_payterm = models.IntegerField()
    due_year_payterm = models.IntegerField()
    deliver = models.CharField(max_length=250)
    is_billed = models.BooleanField(default=False)

    @property
    def total_amount_pay(self):
        total_amount_pay = PaymentEmployee.objects.filter(fk_id_payterm=self.id_payterm).aggregate(Sum('amount_pay'))
        return total_amount_pay['amount_pay__sum'] or 0
    
    def __str__(self):
        return f"PaymentTerm {self.id_payterm}"
    
class PaymentEmployee(models.Model):
    id_pay = models.AutoField(primary_key=True)
    fk_id_payterm = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE)
    fk_id_em = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    hours_pay = models.IntegerField()
    task = models.TextField()
    is_delivered = models.BooleanField(default=False)

    @property
    def amount_pay(self):
        return (self.fk_id_em.fk_id_cg.hourly_wage_cg * self.hours_pay)

    def __str__(self):
        return f"PaymentEmployee {self.id_pay}"

"""
class Expense(models.Model):
    id_expense = models.AutoField(primary_key=True)
    fk_id_payterm = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE) 
    description_expense = models.TextField(max_length=2000)
    amount_expense = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Expense {self.id_expense}"
"""