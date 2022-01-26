from django.urls import path
from .views import *
urlpatterns = [
    path('mainCourse/',mainCoursePage,name='mainCourse'),
    path('contactPage/',contactPage,name="contactPage"),
    path('aboutPage/',aboutPage,name='aboutPage'),
    path('courseContent/',courseContent,name='courseContent'),
    path('particularCourse/<int:id>/',particularCourse,name= 'particularCourse')
]
