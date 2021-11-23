from django.urls import path
from .views import loginFunction,registerFunction,home,verifyUser
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',loginFunction,name="login"),
    path('reg/',registerFunction,name="reg"),
    path('home/',home,name='home'),
    path('verify/',verifyUser,name="verify"),
    # path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='html/reset_password_form.html'),name='password_reset'), #submit email form
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='html/password_reset_done.html'),name='password_reset_done'), # email sent success message for user
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='html/password_reset_complete.html'),name='password_reset_confirm'), # link is sent to email to reset password
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='html/password_reset_complete_done.html'),name='password_reset_complete'), #password successfully changed message


]
