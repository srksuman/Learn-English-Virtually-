from django.urls import path
from .views import loginFunction,registerFunction,home

urlpatterns = [
    path('login/',loginFunction,name="login"),
    path('reg/',registerFunction,name="reg"),
    path('home/',home,name='home'),
]
