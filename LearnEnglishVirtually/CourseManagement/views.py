from django.shortcuts import render
from .models import MainContent,EnglishDictionary
import random
from PyDictionary import PyDictionary
# Create your views here.

def mainCoursePage(request):
    # with open("words.txt", "r") as fil:
    #     for line in fil:
    #         word = line.strip()
    #         EnglishDictionary.objects.create(word = word)
    # try:
    list_of_words = [j for i in EnglishDictionary.objects.values_list('word') for j in i]
    word = random.sample(list_of_words,1)[0]
    print(word)
    dictionary=PyDictionary()
    print (dictionary.meaning(word))
    # except:
    #     pass
    # print (dictionary.synonym(word))
    # print (dictionary.antonym(word))
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

def particularCourse(request,slug):
    allCourses = MainContent.objects.get(slug=slug)
    context = {
    'TopPageName':f'{allCourses.id}. {allCourses.topic}',
    'pageName':'Courses',
    'allCourses':allCourses,
    }
    return render(request,'html/particularCourse.html',context)