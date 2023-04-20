from django.db import models
from django.utils import timezone
from datetime import date,timedelta

# Create your models here.
class Bill(models.Model):
    clientname=models.CharField(primary_key=True,max_length=150, null=False, blank=False,)
    project_cost=models.PositiveIntegerField(default=0, null=True, blank=True)
    tax=models.PositiveIntegerField(default=0)
    total_cost=models.PositiveIntegerField(default=0,unique=False)
    created_date = models.DateTimeField(default=timezone.now)
    

    def save(self, *args, **kwargs):
        Value_Added_Tax=0.16
        self.tax=(int(self.project_cost)) * Value_Added_Tax
        self.total_cost=(int(self.tax) + int(self.project_cost))
        return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.clientname
    

class Receipts(models.Model):
    mode=[
        ('MPESA ', 'Mpesa'),
        ('Cheque', 'Cheque'),
        ('Banking','Bank Payment')
    ]

    id=models.BigAutoField(primary_key=True)
    invoice=models.ForeignKey(Bill, null=True, on_delete=models.CASCADE,unique=False)
    transaction_date = models.DateField(default=timezone.now)
    amt_paid=models.PositiveIntegerField(default=0)
    payment_mode=models.CharField(max_length=20,choices=mode, default='Mpesa')
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.invoice}'
    
class Account(models.Model):
    id=models.BigAutoField(primary_key=True)
    facility_name=models.ForeignKey(Receipts, null=True, on_delete=models.CASCADE)
    town=models.CharField(max_length=100, null=False, blank=False,)
    county=models.CharField(max_length=70, null=False, blank=False,)
    start_date = models.DateField(null=True, blank=True)
    golive_date=models.DateField(null=True, blank=True)
    end_date= models.DateField(null=True, blank=True)
    no_of_days=models.CharField(max_length=30,blank=True)
    license_due=models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.no_of_days=self.end_date - self.start_date
        self.license_due=self.golive_date + timedelta(days=366)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.facility_name}'
    
class Report(models.Model):
    name = models.ForeignKey(Receipts,null=True, on_delete=models.CASCADE)
    project_cost=models.PositiveIntegerField(default=0)
    paid=models.PositiveIntegerField(default=0)
    balance=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'