from django.test import TestCase
from authentication.models import PreRegistration

class TestModel(TestCase):
    def test_model_str(self):
        first_name = PreRegistration.objects.create(first_name="Suman")
        last_name = PreRegistration.objects.create(last_name="Raj")
        self.assertEqual(first_name.__str__()+last_name.__str__(),'Suman  Raj')