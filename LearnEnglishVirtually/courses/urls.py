from django.urls import path
from .views import *
urlpatterns = [
    path('mainCourse/',mainCoursePage,name='mainCourse'),
    path('contactPage/',contactPage,name="contactPage"),
]
