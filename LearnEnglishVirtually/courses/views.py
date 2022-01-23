from django.shortcuts import render
from .models import SubContent
# Create your views here.
def courseDisplay(request):
    return render(request,'html/index.html')