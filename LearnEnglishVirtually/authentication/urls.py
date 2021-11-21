from django.urls import path
from .views import loginFunction,registerFunction

urlpatterns = [
    path('login/',loginFunction,name="login"),
    path('reg/',registerFunction,name="reg")
]
