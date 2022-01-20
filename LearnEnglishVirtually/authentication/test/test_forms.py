from django.test import TestCase
from authentication.forms import UserCreation, validate_username, validate_email

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
        get_value = validate_email('sumanrajkhanal@gmail.com')
        self.assertEqual(get_value,None)

        