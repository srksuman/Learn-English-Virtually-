from django.test import TestCase
from courses.views import *
from django.urls import reverse,resolve

class TestViews(TestCase):

    def test_mainCoursePage(self):
        response = self.client.get(reverse('mainCourse'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('html/course.html')

    def test_contactPage(self):
        response = self.client.get(reverse('contactPage'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('html/contact.html')

    def test_aboutPage(self):
        response = self.client.get(reverse('aboutPage'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('html/about.html')

    def test_courseContent(self):
        response = self.client.get(reverse('courseContent'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('html/courses.html')

    def test_particularCourse(self):
        # response = self.client.get(reverse('particularCourse'))
        # self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('html/particularCourse.html')

