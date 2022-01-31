from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *

# class TestManagementListView(ListView):
#     if User.is_authenticated:
#         model = TestManagement 
#         template_name = 'html/content.html'
    

def testManagement(request):
    if request.user.is_authenticated:
        object_list = TestManagement.objects.all()
        return render(request,'html/content.html',{'object_list':object_list})
    else:
        return HttpResponseRedirect('/')

def test_management_view(request, pk):
    if request.user.is_authenticated:
        testMgt = TestManagement.objects.get(pk=pk)
        return render(request, 'html/TestMgmt.html', {'obj': testMgt})
    else:
        return HttpResponseRedirect('/')

def test_data_details_view(request, pk):
    print(request.user)
    if request.user.is_authenticated:
        testMgmt = TestManagement.objects.get(pk=pk)
        questions = []
        for q in testMgmt.get_questions():
            answers = []
            for a in q.get_answers():
                answers.append(a.text)
            questions.append({str(q): answers})
        return JsonResponse({
            'data': questions,
            'time': testMgmt.time,
        })
    else:
        return HttpResponseRedirect('/')


def save_test_management_view(request, pk):
    if request.method == "POST":
        print(request.POST)
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print("suman")
        print(questions)

        user = request.user
        testMgmt = TestManagement.objects.get(pk=pk)

        score = 0
        multiplier = 100 / testMgmt.number_of_questions
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})   
        score_ = score * multiplier
      
        Result.objects.create(TestMgmt=testMgmt, user=user, score=score_)
        if score_ >= testMgmt.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
    else:
        return JsonResponse({'Error': 404})