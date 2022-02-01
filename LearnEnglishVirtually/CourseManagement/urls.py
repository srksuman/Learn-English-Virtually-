from django.urls import path
from .views import *

urlpatterns = [
    path('',mainCoursePage,name='main'),
    path('contact/',contactPage,name="contact"),
    path('about/',aboutPage,name='about'),
    path('course/',courseContent,name='course'),
    path('progress/',studentProgress,name='progress'),
    path('particularCourse/<slug>/',particularCourse,name= 'particularCourse'),

]
