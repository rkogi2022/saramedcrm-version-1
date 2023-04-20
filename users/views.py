from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm



# Create your views here.
def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('users:login')
        else:
            return HttpResponse('Incorrect Form Formart')
    else:
        return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been update!')
            return redirect('users:profile')
    else:
        u_form=UserUpdateForm(request.POST,instance=request.user)
    return render(request,'users/profile.html',{'u_form':u_form})
