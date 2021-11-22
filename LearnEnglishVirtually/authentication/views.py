from django.contrib.auth import authenticate, forms, login, logout
from django.shortcuts import render
from .forms import UserCreation,LoginForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def registerFunction(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreation(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account is created Successfully!')
        else:
            form = UserCreation()
        return render(request,'html/register.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')


def loginFunction(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request = request,data = request.POST)
            if form.is_valid():
                print("Worked")
                username = form.cleaned_data['username']
                pas = form.cleaned_data['password']
                usr = authenticate(username= username,password=pas)
                login(request,usr)
                return HttpResponseRedirect('/home/')
        else:
            form = LoginForm()
        return render(request,'html/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')

def home(reqest):
    if reqest.user.is_authenticated:
        return render(reqest,'html/home.html')
    else:
        return HttpResponseRedirect('/')

def logoutFun(request):
    logout(request)
    return HttpResponseRedirect('/')