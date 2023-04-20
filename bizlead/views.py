from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from .models import BizLead
from .forms import AddNewBizleadForm, AddDemoForm
from .models import Demo




# Create your views here.
def businesslead(request):
    businessdetails=BizLead.objects.all().order_by('-lead_id')
    p=Paginator(businessdetails,6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render (request, 'bizlead/initialcontact.html',{'businessdetails':businessdetails,'details':details})




def addbusinesslead(request):
    addnewbusiness=AddNewBizleadForm()
    if request.method == 'POST':
        addnewbusiness=AddNewBizleadForm(request.POST)
        if addnewbusiness.is_valid():
            addnewbusiness.save()
            messages.success(request, 'Prospect added successfully!!')
            return redirect('bizlead:businesslead')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'bizlead/addbusiness.html',{'addnewbusiness_form':addnewbusiness})
    
def adddemo(request):
    adddemodetails=AddDemoForm()
    if request.method == 'POST':
        adddemodetails=AddDemoForm(request.POST)
        if adddemodetails.is_valid():
            adddemodetails.save()
            messages.success(request, 'Demo details added successfully!!')
            return redirect('bizlead:tracker')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request, 'bizlead/adddemo.html',{'adddemodetails_form':adddemodetails})
    
def facilitydetails(request,id):

    demodetails=Demo.objects.filter(id=id)
    context={
        'facilitydetails':facilitydetails,
        'demodetails':demodetails
    }
    return render(request,'bizlead/conversions.html',context)

def tracker(request):
    demodetails=Demo.objects.all().order_by('-demo_id')
    p=Paginator(demodetails,6)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    details=p.get_page(page_number)
    return render(request,'bizlead/progress.html',{'demodetails':demodetails, 'details':details})

def details_update(request, pk):
    demodetails=Demo.objects.get(id=pk)
    if request.method == 'POST':
        form=AddDemoForm(request.POST, instance=demodetails)
        if form.is_valid():
            form.save()
            return redirect('bizlead:tracker')
    else:
        form=AddDemoForm(instance=demodetails)
    context={
        'form':form,
        }

    return render(request,'bizlead/detailsupdate.html',context)