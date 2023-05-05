from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from support.models import support 
from accounts.models import Account
from .forms import NewUserForm
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

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("support:supportcall")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="registration/login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Account was created for' + user )
			return redirect("support:supportcall")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("overview:login")