from django.urls import path
from .views import *
from authentication.views import *
urlpatterns = [
    path('mainCourse/',mainCoursePage,name='mainCourse'),
    path('contactPage/',contactPage,name="contactPage"),
    path('aboutPage/',aboutPage,name='aboutPage'),
    path('courseContent/',courseContent,name='courseContent'),
    path('particularCourse/<slug>/',particularCourse,name= 'particularCourse'),
    path('login/',loginFunction,name="login"),
    path('reg/',registerFunction,name="reg"),
]
