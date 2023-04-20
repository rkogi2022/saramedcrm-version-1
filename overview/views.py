from django.shortcuts import render
from support.models import support 
from accounts.models import Account
# Create your views here.
def index(request):  

    totaldata=Account.objects.all().count()

    pendingcount = support.objects.filter(status__contains='PENDING').count()
    donecount = support.objects.filter(status__contains='DONE').count()

    registercount = support.objects.filter(module__contains='PATIENT REGISTER').count()
    nursecount = support.objects.filter(module__contains='NURSE').count()
    doctorcount = support.objects.filter(module__contains='DOCTOR').count()
    labcount = support.objects.filter(module__contains='LABORATORY').count()
    radiographycount = support.objects.filter(module__contains='RADIOGRAPHY').count()
    inpatientcount = support.objects.filter(module__contains='INPATIENT').count()
    pharmacycount = support.objects.filter(module__contains='PHARMACY').count()
    cashiercount = support.objects.filter(module__contains='CASHIER').count()
    inventorycount = support.objects.filter(module__contains='INVENTORY').count()
    financecount = support.objects.filter(module__contains='FINANCE').count()
    humancount = support.objects.filter(module__contains='HUMAN RESOURCE').count()
    systemcount = support.objects.filter(module__contains='SYSTEM ADMIN').count()
    

    context={
        'totaldata':totaldata,

        'pendingcount':pendingcount,
        'donecount':donecount,

        'registercount':registercount,
        'nursecount':nursecount,
        'doctorcount':doctorcount,
        'labcount':labcount,
        'radiographycount':radiographycount,
        'inpatientcount':inpatientcount,
        'pharmacycount':pharmacycount,
        'cashiercount':cashiercount,
        'inventorycount':inventorycount,
        'financecount':financecount,
        'humancount':humancount,
        'systemcount':systemcount
    }
    return render(request, 'overview/dashboard.html',context)