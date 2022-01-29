from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import *

class TestManagementListView(ListView):
    model = TestManagement 
    template_name = 'html/main.html'

def test_management_view(request, pk):
    testMgt = TestManagement.objects.get(pk=pk)
    return render(request, 'quiz.html', {'obj': testMgt})

def test_details_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })