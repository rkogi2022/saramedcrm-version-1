from django.db import models
from django.utils import timezone

# Create your models here.
class BizLead(models.Model):
    lead_id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    contact_person=models.CharField(max_length=100)
    contact_phone=models.CharField(max_length=100)
    comment=models.TextField(blank=True)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'
    
class Demo(models.Model):

    meeting=[
        ('PHYSICAL', 'PHYSICAL'),
        ('VIRTUAL', 'VIRTUAL'),
    ]
    status=[
        ('DONE', 'DONE'),
        ('PENDING', 'PENDING'),
    ]
    demo_id=models.ForeignKey(BizLead,null=True, on_delete=models.CASCADE)
    demostatus=models.CharField(max_length=30,choices=status,default='PENDING')
    demodate=models.DateField(null=True, blank=True, default=None)
    Attendees=models.TextField(blank=True)
    meeting=models.CharField(max_length=30,choices=meeting,blank=True)
    feedback=models.TextField(blank=True)

    assessmentdate=models.DateField(null=True, blank=True, default=None)
    report=models.FileField(upload_to='documents/' ,blank=True)
    reportdate=models.DateField(null=True, blank=True, default=None)

    expression=models.FileField(upload_to='documents/' ,blank=True)
    facility_license=models.FileField(upload_to='documents/' ,blank=True)
    krapin=models.FileField(upload_to='documents/' ,blank=True)

    def __str__(self):
        return f'{self.demo_id}'