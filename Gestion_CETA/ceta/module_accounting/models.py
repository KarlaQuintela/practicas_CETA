# module_accounting/models.py
from django.db import models
from ceta.module_contract.models import PaymentTerm

class Bill(models.Model):
    id_bill = models.AutoField(primary_key=True)
    fk_id_payterm = models.ForeignKey(PaymentTerm, on_delete=models.CASCADE) 
    month_bill = models.IntegerField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill {self.id_bill}"

class Receipt(models.Model):
    id_rec = models.AutoField(primary_key=True)
    amoun_rec = models.DecimalField(max_digits=10, decimal_places=2)
    fk_id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    payment_date_rec = models.DateField()

    def __str__(self):
        return f"Receipt {self.id_rec}"

class Remuneration(models.Model):
    id_rem = models.AutoField(primary_key=True)
    amount_rem = models.DecimalField(max_digits=10, decimal_places=2)
    fk_id_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    payment_date_rem = models.DateField()

    def __str__(self):
        return f"Remuneration {self.id_rem}"