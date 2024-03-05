# module_contract/models.py
from django.db import models
from .module_human_resources.models import Worker

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name_client = models.CharField(max_length=255)
    address_client = models.CharField(max_length=255)
    phone_client = models.CharField(max_length=50)
    email_client = models.CharField(max_length=50)
    description_client = models.TextField()

    def __str__(self):
        return self.name_client

class Contract(models.Model):
    id_ct = models.AutoField(primary_key=True)
    num_ct = models.CharField(max_length=255, unique=True)
    title_ct = models.CharField(max_length=255)
    fk_id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_ct = models.DateField()
    end_ct = models.DateField()
    resolution_ct = models.DateField()
    description_ct = models.TextField()
    staff_count = models.IntegerField()
    type_ct = models.CharField(max_length=50)    
    uni_area_ct = models.CharField(max_length=50)
    work_area_ct = models.CharField(max_length=50)
    manager_ct = models.ForeignKey(Worker, on_delete=models.CASCADE)
    value_ct = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2)
    net_income = models.DecimalField(max_digits=10, decimal_places=2)
    currency_ct = models.CharField(max_length=10)
    proposed_by = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=50)
    is_current = models.BooleanField(default=True)

    def __str__(self):
        return self.title_ct

class PaymentTerm(models.Model):
    id_payterm = models.AutoField(primary_key=True)
    fk_id_ct = models.ForeignKey(Contract, on_delete=models.CASCADE) 
    due_month_payterm = models.IntegerField()
    due_year_payterm = models.IntegerField()
    deliver = models.CharField(max_length=50)
    is_billable = models.BooleanField(default=False)

    def __str__(self):
        return f"PaymentTerm {self.id_payterm}"

class PaymentWorker(models.Model):
    id_payworker = models.AutoField(primary_key=True)
    fk_id_w = models.ForeignKey(Worker, on_delete=models.CASCADE) 
    fk_id_payterm = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE) 
    hours_payworker = models.IntegerField()
    percent_payworker = models.DecimalField(max_digits=10, decimal_places=2)
    task_worker = models.TextField()
    amount_payworker = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"PaymentWorker {self.id_payworker}"

class Expense(models.Model):
    id_expense = models.AutoField(primary_key=True)
    fk_id_payterm = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE) 
    description_expense = models.CharField(max_length=255)
    amount_expense = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Expense {self.id_expense}"