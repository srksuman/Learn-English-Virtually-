from django.test import TestCase
from authentication.forms import UserCreation, validate_username, validate_email, LoginForm, VerifyForm, ChangePasswordUserForm,UserUpdateForm
from django.contrib.auth.models import User

class TestForms(TestCase):
    def test_filled_UserCreation(self):
        form = UserCreation(data={
            'password1':'##@Vick9863!!!',
            'password2':'##@Vick9863!!!',
            'username':'SumanRaj',
            'email':'sumanrajkhanal@gmail.com',
            'first_name':'Suman',
            'last_name':'Khanal'
        })
        self.assertTrue(form.is_valid())

    def test_Empty_UserCreation(self):
        form = UserCreation(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),6)

    def test_validate_username(self):
        get_value = validate_username('srk')
        self.assertEqual(get_value,None)

    def test_validate_email(self):
        get_value = validate_email('unnittesing@gmail.com')
        self.assertEqual(get_value,None)

    def test_LoginForm(self):
        form = LoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)

    def test_VerifyForm(self):
        form = VerifyForm(data={})
        fm = VerifyForm(data={'otp':12563})
        self.assertTrue(fm.is_valid())
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_ChangePasswordUserForm(self):
        form = ChangePasswordUserForm(User,data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)

    def test_UserUpdateForm(self):
        form = UserUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),3)