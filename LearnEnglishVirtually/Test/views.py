from django.shortcuts import render
from .models import *
# from django.views.generic import ListView
# # Create your views here.

# class TestManagementList(ListView):
#     model = TestManagement
#     # context_object_name = ''
#     template_name='html/main.html'

# def test_view(request,id):
#     test = TestManagement.objects.get(pk=id)
#     return render(request,'',{'obj':test})


# def testContent(request):
#     test = TestManagement.objects.all()
#     return render(request,'html/testContent.html',{'test':test})