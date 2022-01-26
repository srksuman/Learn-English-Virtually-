from django.test import TestCase
from courses.models import MainContent

class TestModel(TestCase):
    def test_model_str(self):
        topic = MainContent.objects.create(topic="Articles")
        self.assertEqual(topic.__str__(),'Articles')