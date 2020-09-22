from django.shortcuts import render
from . import views
#from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import SignupForm, LeaveDataForm
from .models import LeaveData
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'leave/home.html')

def about(request):
    return render(request,'leave/about.html')


def contactus(request):
    return render(request,'leave/contactus.html')

def register(request):
    form = SignupForm()
    if request.method == "POST":
        print(request.method)
        form = SignupForm(request.POST)
        if form.is_valid():
            role = request.POST.get('role')
            print(role)
            user = form.save()

            if role == "Manager" or "manager":
                group = Group.objects.get(name="manager")
                user.groups.add(group)
            else:
                group = Group.objects.get(name="employee")
                user.groups.add(group)
            return HttpResponseRedirect('/login/')
    else:
        form = SignupForm()
    return render(request,'leave/register.html',{'form':form})

def login_url(request):
    form = AuthenticationForm()
    if request.method == "POST":
        print(request.method)
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            print(form.is_valid())
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/lstatus/')
    else:
        form = AuthenticationForm()
    return render(request,'leave/login.html', {'form':form})

@login_required
def lstatus(request):
    if request.user.is_authenticated:
        ldetails = LeaveData.objects.all()
        return render(request,'leave/lstatus.html',{'ldetails':ldetails, 'user':request.user})
    else:
        return HttpResponseRedirect('/login/')

@login_required
def logout_url(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request,'leave/home.html')

@login_required
def leaveform(request):
    form = LeaveDataForm()
    if request.method == "POST":
        print(request.method)
        form = LeaveDataForm(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return HttpResponseRedirect('/lstatus/')
    else:
        form = LeaveDataForm()
    #return render(request,'leave/register.html',{'form':form})

    return render(request,'leave/leaveform.html', {'form':form})

@login_required
def approve_leave(request, id):
    if request.user.is_authenticated:
        if request.method== "POST":
            obj = LeaveData.objects.filter(pk=id)
            obj.update(leave_status="Approved")
            leavedays=0
            for eachobj in obj:
                leavedays=eachobj.leave_days
                leavebal=eachobj.leave_bal
                updatedleavebal = leavebal - leavedays
            obj.update(leave_bal=updatedleavebal)
            for eachobj in obj:
                eachobj.save()


            return HttpResponseRedirect('/lstatus/')
        return HttpResponseRedirect('/lstatus/')


@login_required
def decline_leave(request,id):

    if request.method== "POST":
        obj = LeaveData.objects.filter(pk=id)
        print(obj)
        obj.update(leave_status="Declined")
        for eachobj in obj:
            eachobj.save()
        #obj.save()
        return HttpResponseRedirect('/lstatus/')
    return HttpResponseRedirect('/lstatus/')
