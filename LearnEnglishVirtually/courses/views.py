from django.shortcuts import render
from .models import MainContent
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
    allCourses = MainContent.objects.all()
    context = {
    'TopPageName':"Our Courses",
    'pageName':'Courses',
    'allCourses':allCourses,
    }
    
    return render(request,'html/courses.html',context)

def particularCourse(request,id):
    allCourses = MainContent.objects.get(id=id)
    context = {
    'TopPageName':f'{allCourses.id}. {allCourses.topic}',
    'pageName':'Courses',
    'allCourses':allCourses,
    }
    return render(request,'html/particularCourse.html',context)