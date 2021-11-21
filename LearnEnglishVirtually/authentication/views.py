from django.shortcuts import render

# Create your views here.
def loginFunction(request):
    return render(request,'html/login.html')

def registerFunction(request):
    return render(request,'html/register.html')