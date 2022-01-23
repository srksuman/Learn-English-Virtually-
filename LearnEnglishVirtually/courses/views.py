from django.shortcuts import render
from .models import SubContent
# Create your views here.
def mainCoursePage(request):
    return render(request,'html/index.html')

def contactPage(request):
    context = {
    'TopPageName':"Contact Us",
    'pageName':'Contact'
    }
    return render(request,'html/contact.html',context)

def aboutPage(request):
    context = {
    'TopPageName':"About Us",
    'pageName':'About'
    }
    return render(request,'html/about.html',context)

def courseContent(request):
    context = {
    'TopPageName':"Our Courses",
    'pageName':'Courses'
    }
    return render(request,'html/courses.html',context)