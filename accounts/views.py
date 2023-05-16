from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum, Count

from .models import Bill
from .forms import AddNewBill
from .models import Receipts
from .forms import CreateReceipt
from .models import Account, Report
from .forms import AddClient

#create your views here
def bills(request):
    billingdetails=Bill.objects.all().order_by('-created_date')
    p=Paginator(billingdetails,6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request, 'accounts/bill.html', {'billingdetails':billingdetails,'details':details})

def addnewbill(request):
    addnewbill=AddNewBill()
    if request.method == 'POST':
        addnewbill=AddNewBill(request.POST)
        if addnewbill.is_valid():
            addnewbill.save()
            messages.success(request, f'Billing created successfully!!')
            return redirect('accounts:bills')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'accounts/addbill.html',{'addnewbill_form':addnewbill})

def receipts(request):
    paid_amount= Receipts.objects.aggregate(Sum('amt_paid'))
    receiptsdetails=Receipts.objects.all().order_by('-id')
    p=Paginator(receiptsdetails,6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request,'accounts/receipts.html',{'paid_amount':paid_amount,'receiptsdetails':receiptsdetails,'details':details})

def addreceipt(request):
    addreceipt=CreateReceipt()
    if request.method == 'POST':
        addreceipt=CreateReceipt(request.POST)
        if addreceipt.is_valid():
            addreceipt.save()
            messages.success(request, f'Receipt Added successfully!!')
            return redirect('accounts:receipts')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'accounts/addreceipt.html',{'addreceipt_form':addreceipt})
    
def addreceipt_delete(request, id):
    receiptsdetails=Receipts.objects.filter(id=id)
    if request.method == 'POST':
        receiptsdetails.delete()
        return redirect('accounts:receipts')
    return render(request,'accounts/delete.html')
    
def addreceipt_update(request, id):
    receiptsdetails=Receipts.objects.get(pk=id)
    if request.method == 'POST':
        form=CreateReceipt(request.POST, instance=receiptsdetails)
        if form.is_valid():
            form.save()
            return redirect('accounts:receipts')
    else:
        form=CreateReceipt(instance=receiptsdetails)
    context={
        'form':form,
        }

    return render(request,'accounts/detailsupdate.html',context)

def reports(request):
    name_details=Bill.objects.values('clientname','total_cost')
    totalamt=Receipts.objects.values('invoice').annotate(Sum('amt_paid'))

    for key in totalamt:
        print('Key=',key)
        
    # p=Paginator(reportdetails,6)
    # # getting the desired page number from url
    # page_number = request.GET.get('page')
    # details=p.get_page(page_number)
    context={
        'name_details':name_details,
        'totalamt':totalamt

        #'details':details
        }
    return render(request,'accounts/reports.html',context)


def accdetails(request):
    clientdetails=Account.objects.all().order_by('-id')
    p=Paginator(clientdetails,6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request, 'accounts/clientaccount.html', {'clientdetails':clientdetails,'details':details})

def addclientacc(request):
    addnewclient=AddClient()
    if request.method == 'POST':
        addnewclient=AddClient(request.POST)
        if addnewclient.is_valid():
            addnewclient.save()
            messages.success(request, f'Account created successfully!!')
            return redirect('accounts:accdetails')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'accounts/addclientaccount.html',{'addnewclient_form':addnewclient})
    
def addclientacc_delete(request, id):
    clientdetails=Account.objects.filter(id=id)
    if request.method == 'POST':
        clientdetails.delete()
        return redirect('accounts:accdetails')
    return render(request,'accounts/delete.html')
    
def addclientacc_update(request, id):
    clientdetails=Account.objects.get(pk=id)
    if request.method == 'POST':
        form=AddClient(request.POST, instance=clientdetails)
        if form.is_valid():
            form.save()
            return redirect('accounts:accdetails')
    else:
        form=AddClient(instance=clientdetails)
    context={
        'form':form,
        }

    return render(request,'accounts/detailsupdate.html',context)

def implementation(request, id):
    details=Account.objects.filter(id=id)
    return render(request, 'accounts/implementation.html', {'details':details})
