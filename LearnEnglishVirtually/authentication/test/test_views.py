# from django.test import TestCase
# from authentication.views import creatingOTP,sendEmail
# from django.urls import reverse,resolve
# from django.contrib.auth.models import User

# class TestViews(TestCase):
#     def test_creatingOTP(self):
#         otp_length = len(creatingOTP())
#         self.assertEqual(otp_length,5)

#     def test_sendEmail(self):
#         otp = len(sendEmail("sumanrajkhanal@gmail.com","suman"))
#         self.assertEqual(otp,5)

#     def test_register_get_function(self):
#         response = self.client.get(reverse('reg'))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed('html/register.html')

#     def test_register_post_function(self):
#         response = self.client.post(reverse('reg'),{
#             'username':'test',
#             'first_name':'test',
#             'password':'##@0hyu12'
#         })
#         self.assertEqual(response.status_code,200)

#     def test_get_loginFunction(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed('html/login.html')

#     def test_post_login_function(self):
#         response = self.client.post(reverse('login'),{
#             'username':'test',
#             'password':'##@0hyu12'
#         })
#         self.assertEqual(response.status_code,200)

#     def test_verify_user(self):
#         response = self.client.get(reverse('verify'))
#         self.assertEqual(response.status_code,200)
#         self.assertTemplateUsed('html/verify.html')

#     def test_home_function(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code,302)
#         self.assertTemplateUsed('html/home.html')

#     def test_logout_function(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code,302)

#     def test_changePassword(self):
#         User.objects.create(username='test',email='sumankhanal@gmail.com',password='hfa3473bb!!2')
#         response = self.client.get(reverse('changePassword'))
#         response_post = self.client.post(reverse('changePassword'),{'old_password':'hfa3473bb!!2','new_password1':'dhfa6@76##','new_password2':'dhfa6@76##'})
#         self.assertEqual(response.status_code,302)
#         self.assertEqual(response_post.status_code,302)
#         self.assertTemplateUsed('html/changePassword.html')
    
#     def test_update_user_profile(self):
#         self.assertEqual(self.client.post(reverse('updateUserProfile')).status_code,302)
#         self.assertTemplateUsed('html/updateProfile.html')
    
    
        