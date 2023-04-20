from django.db import models
from django.utils import timezone
from accounts.models import Receipts

# Create your models here.
class support(models.Model):
    module=[
        ('PATIENT REGISTER', 'PATIENT REGISTER'),
        ('NURSE', 'NURSE'),
        ('DOCTOR','DOCTOR'),
        ('LABORATORY','LABORATORY'),
        ('RADIOGRAPHY','RADIOGRAPHY'),
        ('INPATIENT','INPATIENT'),
        ('PHARMACY','PHARMACY'),
        ('CASHIER','CASHIER'),
        ('INVENTORY','INVENTORY'),
        ('FINANCE','FINANCE'),
        ('HUMAN RESOURCE','HUMAN RESOURCE'),
        ('SYSTEM ADMIN','SYSTEM ADMIN'),
    ]
    status=[
        ('PENDING ','PENDING'),
        ('DONE','DONE'),
    ]
    id=models.BigAutoField(primary_key=True)
    facility=models.ForeignKey(Receipts, null=True, on_delete=models.CASCADE)
    logdate=models.DateField(default=timezone.now)
    module=models.CharField(max_length=30,choices=module, default='PATIENT REGISTER')
    problem=models.TextField(null=True,blank=True)
    solution=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=20,choices=status, default='DONE')
    completiondate=models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.facility}'
    

class courtesy(models.Model):
    id=models.BigAutoField(primary_key=True)
    facility=models.ForeignKey(Receipts, null=True, on_delete=models.CASCADE)
    logdate=models.DateField(default=timezone.now)
    feedback=models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.facility}'

class bimonthly(models.Model):
    id=models.BigAutoField(primary_key=True)
    facility_name=models.ForeignKey(Receipts, null=True, on_delete=models.CASCADE)
    logdate=models.DateField(default=timezone.now)
    feedback_given=models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.facility_name}'