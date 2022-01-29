from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import *

class TestManagementListView(ListView):
    model = TestManagement 
    template_name = 'html/main.html'