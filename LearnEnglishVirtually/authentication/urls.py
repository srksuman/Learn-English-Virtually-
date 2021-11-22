from django.urls import path
from .views import loginFunction,registerFunction,home,verifyUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',loginFunction,name="login"),
    path('reg/',registerFunction,name="reg"),
    path('home/',home,name='home'),
    path('verify/',verifyUser,name="verify"),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]
