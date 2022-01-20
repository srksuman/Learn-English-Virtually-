from django.test import TestCase
from django.urls import reverse,resolve
from authentication.views import home,verifyUser,logoutFun,changePassword,updateUserProfile
from django.contrib.auth import views as auth_views

class TestURL(TestCase):
    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_register(self):
        response = self.client.get(reverse('reg'))
        self.assertEqual(response.status_code,200)

    def test_home(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func,home)

    def test_verify(self):
        url = reverse('verify')
        self.assertEqual(resolve(url).func,verifyUser)

    def test_logout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func,logoutFun)

    def test_reset_password(self):
        url = reverse('password_reset')
        self.assertEqual(resolve(url).func.view_class,auth_views.PasswordResetView)

    def test_reset_password_done(self):
        self.assertEqual(resolve(reverse('password_reset_done')).func.view_class,auth_views.PasswordResetDoneView)

    def test_password_reset_confirm(self):
        self.assertEqual(resolve(reverse('password_reset_confirm',args=['uidb64','token'])).func.view_class,auth_views.PasswordResetConfirmView)
    
    def test_password_reset_complete(self):
        url = reverse('password_reset_complete')
        self.assertEqual(resolve(url).func.view_class,auth_views.PasswordResetCompleteView)
    
    def test_change_password(self):
        url = reverse('changePassword')
        self.assertEqual(resolve(url).func,changePassword)

    def test_updateUserProfile(self):
        url = reverse('updateUserProfile')
        self.assertEqual(resolve(url).func,updateUserProfile)