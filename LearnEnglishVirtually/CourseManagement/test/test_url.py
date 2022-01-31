from django.test import TestCase
from django.urls import reverse,resolve
from courses.views import *

class TestURL(TestCase):
    def test_mainCoursePage(self):
        response = self.client.get(reverse('mainCourse'))
        self.assertEqual(response.status_code,200)

    def test_contactPage(self):
        response = self.client.get(reverse('contactPage'))
        self.assertEqual(response.status_code,200)

    def test_aboutPage(self):
        url = reverse('aboutPage')
        self.assertEqual(resolve(url).func,aboutPage)

    def test_courseContent(self):
        url = reverse('courseContent')
        self.assertEqual(resolve(url).func,courseContent)

    # def test_particularCourse(self):
    #     url = reverse('particularCourse',args=['id'])
    #     self.assertEqual(resolve(url).func,particularCourse)
