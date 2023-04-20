from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .models import support
from .forms import AddNewClient
from .models import courtesy
from .forms import AddCourtesyCall
from .models import bimonthly
from .forms import AddBimonthlyCall
from .resource import supportResource

# Create your views here.
    
def supportcall(request):
        supportdetails=support.objects.all().order_by('-logdate')
        p=Paginator(supportdetails,5)
        # getting the desired page number from url
        page_number = request.GET.get('page')
        details=p.get_page(page_number)
        return render(request, 'support/supportcall.html', {'supportdetails':supportdetails, 'details':details})

def searchbar(request):
    if request.method == 'GET':
        searched=request.GET.get('searched')
        if searched:
            multiple_searched=Q(Q(module__contains=searched) |Q(status__contains=searched))
            searcheddetails=support.objects.filter(multiple_searched)
            return render(request, 'support/search.html',{'searcheddetails':searcheddetails})
        else:
            return render(request, 'support/search.html',{})
        

def addsupportcall(request):
    addsupportcall=AddNewClient()
    if request.method == 'POST':
        addsupportcall=AddNewClient(request.POST)
        if addsupportcall.is_valid():
            addsupportcall.save()
            messages.success(request, 'Support Call Logged Successfully!!')
            return redirect('support:supportcall')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'support/addsupportcall.html',{'addsupportcall_form':addsupportcall})
    

def addsupportcall_delete(request, pk):
    supportdetails=support.objects.filter(id=pk)
    if request.method == 'POST':
        supportdetails.delete()
        return redirect('support:supportcall')
    return render(request,'support/delete.html')
    
def addsupportcall_update(request, pk):
    supportdetails=support.objects.get(id=pk)
    if request.method == 'POST':
        form=AddNewClient(request.POST, instance=supportdetails)
        if form.is_valid():
            form.save()
            return redirect('support:supportcall')
    else:
        form=AddNewClient(instance=supportdetails)
    context={
        'form':form,
        }

    return render(request,'support/update.html',context)


def courtesycall(request):
    courtesydetails=courtesy.objects.all().order_by('-logdate')
    p=Paginator(courtesydetails,5)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request, 'support/courtesycall.html', {'courtesydetails':courtesydetails,'details':details})

def addcourtesycall(request):
    addcourtesycall=AddCourtesyCall()
    if request.method == 'POST':
        addcourtesycall=AddCourtesyCall(request.POST)
        if addcourtesycall.is_valid():
            addcourtesycall.save()
            messages.success(request, 'Courtsey Call Logged Successfully!!')
            return redirect('support:courtesycall')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'support/addcourtesycall.html',{'addcourtesycall_form':addcourtesycall})
    
def addcourtesycall_delete(request, pk):
    courtesydetails=courtesy.objects.filter(id=pk)
    if request.method == 'POST':
        courtesydetails.delete()
        return redirect('support:courtesycall')
    return render(request,'support/delete.html')

def addcourtesycall_update(request, pk):
    courtesydetails=courtesy.objects.get(id=pk)
    if request.method == 'POST':
        form=AddCourtesyCall(request.POST, instance=courtesydetails)
        if form.is_valid():
            form.save()
            return redirect('support:courtesycall')
    else:
        form=AddCourtesyCall(instance=courtesydetails)
    context={
        'form':form,
        }

    return render(request,'support/update.html',context)
    
def bimonthlycall(request):
    bimonthlydetails=bimonthly.objects.all().order_by('-id')
    p=Paginator(bimonthlydetails,5)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request, 'support/directorscall.html', {'bimonthlydetails':bimonthlydetails,'details':details})

def addbimonthlycall(request):
    addbimonthlycall=AddBimonthlyCall()
    if request.method == 'POST':
        addbimonthlycall=AddBimonthlyCall(request.POST)
        if addbimonthlycall.is_valid():
            addbimonthlycall.save()
            messages.success(request, ' Call Logged Successfully!!')
            return redirect('support:bimonthlycall')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'support/adddirectorscall.html',{'addbimonthlycall_form':addbimonthlycall})

def bimonthlycall_delete(request, pk):
    bimonthlydetails=bimonthly.objects.filter(id=pk)
    if request.method == 'POST':
        bimonthlydetails.delete()
        return redirect('support:bimonthlycall')
    return render(request,'support/delete.html')

def bimonthlycall_update(request, pk):
    bimonthlydetails=bimonthly.objects.get(id=pk)
    if request.method == 'POST':
        form=AddBimonthlyCall(request.POST, instance=bimonthlydetails)
        if form.is_valid():
            form.save()
            return redirect('support:bimonthlycall')
    else:
        form=AddBimonthlyCall(instance=bimonthlydetails)
    context={
        'form':form,
        }

    return render(request,'support/update.html',context)



