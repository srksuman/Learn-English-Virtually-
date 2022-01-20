from django.contrib.auth import authenticate, forms, login, logout
from django.shortcuts import render
from .forms import UserCreation,LoginForm,VerifyForm,ChangePasswordUserForm,UserUpdateForm
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User
from .models import PreRegistration

# Create your views here.
def creatingOTP():
    otp = ""
    for i in range(5):
        otp+= f'{random.randint(0,9)}'
    return otp

def sendEmail(email,fname):
    otp = creatingOTP()
    print("Successfully done!!!!!!!!")
    email_message = f"""
Dear Sir/Madam,
{fname}
ATTN : Please do not reply to this email.This mailbox is not monitored and you will not receive a response.
Your One Time Password (OTP ) is {otp}.
If you have any queries, Please contact us at,
learn English Virtually,
Thali,Kathmandu, Nepal.
Phone # 977-9803955983
Email Id: learnenglishvirtually2078@gmail.com
Warm Regards,
Learn English Virtually."""
    send_mail(
    'One Time Password',
    email_message,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
    )
    return otp

def registerFunction(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreation(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                fname = form.cleaned_data['first_name']
                otp = sendEmail(email,fname)
                dt = PreRegistration(first_name=form.cleaned_data['first_name'],last_name=form.cleaned_data['last_name'],username= form.cleaned_data['username'],email=email,otp=otp,password1 = form.cleaned_data['password1'],password2 = form.cleaned_data['password2'])
                dt.save()
                return HttpResponseRedirect('/verify/')
                # form.save()
                # messages.success(request, 'Account is created Successfully!')
        else:
            form = UserCreation()
        return render(request,'html/register.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')


def loginFunction(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request = request,data = request.POST)
            # username = request.POST['username']
            # if '@gmail.com' in username:
            #         print(User.objects.all())
            #         get_user_obj = User.objects.get(email = username)
            #         username = get_user_obj.username
            # pas = request.POST['password']
            # usr = authenticate(username= username,password=pas)
            # login(request,usr)
            # return HttpResponseRedirect('/home/')
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

def verifyUser(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = VerifyForm(request.POST)
            if form.is_valid():
                otp = form.cleaned_data['otp']
                data = PreRegistration.objects.filter(otp = otp)
                if data:
                    username = ''
                    first_name = ''
                    last_name = ''
                    email = ''
                    password1 = ''
                    for i in data:
                        print(i.username)
                        username = i.username
                        first_name = i.first_name
                        last_name = i.last_name
                        email = i.email
                        password1 = i.password1

                    user = User.objects.create_user(username, email, password1)
                    user.first_name = first_name
                    user.last_name = last_name
                    user.save()
                    data.delete()
                    messages.success(request,'Account is created successfully!')
                    return HttpResponseRedirect('/verify/')   
                else:
                    messages.success(request,'One Time Password is wrong')
                    return HttpResponseRedirect('/verify/')
        else:            
            form = VerifyForm()
        return render(request,'html/verify.html',{'form':form})
    else:
        return HttpResponseRedirect('/success/')

def home(reqest):
    if reqest.user.is_authenticated:
        return render(reqest,'html/home.html')
    else:
        return HttpResponseRedirect('/')

def logoutFun(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def changePassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            changePasswordForm = ChangePasswordUserForm(user=request.user,data= request.POST)
            if changePasswordForm.is_valid():
                changePasswordForm.save()
                messages.success(request,"Your password is changed successfully,")
                return HttpResponseRedirect('/login/')
                
        else:
            changePasswordForm = ChangePasswordUserForm(user=request.user)
        return render(request,'html/changePassword.html',{'form':changePasswordForm})
    else:
        return HttpResponseRedirect('/login/')

def updateUserProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserUpdateForm(request.POST,instance= request.user)
            uname = request.POST['username']
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            # checkUname = User.objects.filter(username=uname)
            # if(checkUname):
            #     if(checkUname.email == request.user.email ):
            #         print("success")
            User.objects.filter(email=request.user.email).update(username=uname,first_name=fname,last_name=lname)
            messages.success(request,"Your profile is updated successfully")
            if form.is_valid():
                User.objects.filter(username=request.user.username).update(username="sumanraj")
                form.save()
                messages.success(request,"Your profile is updated successfully")
                return HttpResponseRedirect('/updateUserProfile/')
        else:        
            form = UserUpdateForm(instance= request.user)
        return render(request,'html/updateProfile.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

