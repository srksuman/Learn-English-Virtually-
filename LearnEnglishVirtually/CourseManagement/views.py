from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import MainContent,EnglishDictionary
import random
from PyDictionary import PyDictionary
import json
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from TestManagement.models import Result
from django.contrib import messages

# Create your views here.

def mainCoursePage(request):
    # with open("words.txt", "r") as fil:
    #     for line in fil:
    #         word = line.strip()
    #         EnglishDictionary.objects.create(word = word)
    try:
        list_of_words = [j for i in EnglishDictionary.objects.values_list('word') for j in i]
        word = random.sample(list_of_words,1)[0]
        print(word)
        dictionary=PyDictionary()
        print (dictionary.meaning(word))
    except:
        pass

    # f=open("data.js")
    # data = json.load(f)
    # for i in data:
        # print(i['id'])
        # MainContent.objects.create(id=i['id'],topic = i['topic'],content = i['content'],estimated_time=i['estimated_time'],sub_topic=i['sub_topic'])
    # print (dictionary.synonym(word))
    # print (dictionary.antonym(word))
    return render(request,'html/index.html')

def contactPage(request): 
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['Subject']
        form = ContactForm(request.POST)
        
        if form.is_valid():
            email_message=f"""
            Name: {name}
            Message: {message}
            Email: {email}
            """
            messages.info(request,f"Dear! {name} your message has been received we'll get back you shortly!!!")
            send_mail(
            f'Message From LEV:- {subject}',
            email_message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
            )
            return HttpResponseRedirect('/contact/')

    else:
        form = ContactForm()
    return render(request,'html/contact.html',{
        'form':form,
         })

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


def studentProgress(request):
    result = Result.objects.filter(user=request.user)
    number_of_test_given = len(result)
    # print(result.count())
    # print(Result.objects.latest('id'))

    #find the testmanagement id when test are qizen and how many times
    name_of_topic = ''
    name_of_topic_num = 0
    count_number_of_particular_given_test = {}
    
 
    list_of_time_passed = []
    list_of_time_failed = []
    list_of_topic_passed_failed = []

    list_of_given_test = []
    list_of_given_test_score_highest=[]
    list_of_given_test_score_lowest=[]
    collect_topic_object_length = 0
    try:
        #how many time a user passed or failed a particular topic
        collect_topic_object = list(dict.fromkeys([ i.TestMgmt for i in result]))
        collect_topic_object_length = len(collect_topic_object)
        list_of_topic_passed_failed += [i.topic.topic for i in collect_topic_object]
        list_of_given_test += list_of_topic_passed_failed
        for i in collect_topic_object:
            list_of_given_test_score_highest.append(max([i.score for i in Result.objects.filter(score__gte = 50, user = request.user,TestMgmt=i)]))
            list_of_given_test_score_lowest.append(max([i.score for i in Result.objects.filter(score__lt = 49, user = request.user,TestMgmt=i)]))
            failed_times = len(Result.objects.filter(score__lt = 49, user = request.user,TestMgmt=i))
            passed_times = len(Result.objects.filter(score__gte = 50, user = request.user,TestMgmt=i))
            list_of_time_passed.append(passed_times)
            list_of_time_failed.append(failed_times)


        number_of_test_given_with_id = [i['TestMgmt_id'] for i in list(result.values('TestMgmt_id'))]
        count_number_of_particular_given_test = {}

        for i in number_of_test_given_with_id:
            if i not in count_number_of_particular_given_test:
                count_number_of_particular_given_test[i] = 1
            else:
                count_number_of_particular_given_test[i] +=1

        get_id_of_max_given_test = max(zip(count_number_of_particular_given_test.values(),count_number_of_particular_given_test.keys()))[1]
        name_of_topic_num = max(zip(count_number_of_particular_given_test.values(),count_number_of_particular_given_test.keys()))[0]
        name_of_topic = MainContent.objects.get(id=get_id_of_max_given_test).topic
    except:
        name_of_topic = 'Not Given Test'

    flag_failed = 0
    flag_passed = 0

    for i in result:
        if i.score >= 50:
            flag_passed +=1
        else:
            flag_failed +=1
    
    list_of_topics_test_given = []
    list_of_times_test_given = []

    if len(count_number_of_particular_given_test)!=0:
        list_of_times_test_given += list(count_number_of_particular_given_test.values())
        for i in count_number_of_particular_given_test.keys():
            list_of_topics_test_given.append(MainContent.objects.get(id=i).topic)


    context = {
        'number_of_test_given':number_of_test_given,
        'flag_failed':flag_failed,
        'flag_passed':flag_passed,
        'name_of_topic':name_of_topic,
        'name_of_topic_num':name_of_topic_num,
        'list_of_topics_test_given':list_of_topics_test_given,
        'list_of_times_test_given':list_of_times_test_given,
        'list_of_time_passed':list_of_time_passed ,
        'list_of_time_failed':list_of_time_failed,
        'list_of_topic_passed_failed':list_of_topic_passed_failed,
        'list_of_given_test':list_of_given_test,
        'list_of_given_test_score_highest':list_of_given_test_score_highest,
        'list_of_given_test_score_lowest':list_of_given_test_score_lowest,
        'collect_topic_object_length':collect_topic_object_length,
        'zip_list':zip(list_of_given_test,list_of_time_passed,list_of_time_failed,
        list_of_given_test_score_highest,list_of_given_test_score_lowest,)
    }

    return render(request,'html/progress.html',context)



