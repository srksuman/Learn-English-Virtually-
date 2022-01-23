from django.shortcuts import render
from .models import SubContent
# Create your views here.
def mainCoursePage(request):
    return render(request,'html/index.html')

def contactPage(request):
    pageName = "Contact"
    
    return render(request,'html/contact.html',{'pageName':pageName})