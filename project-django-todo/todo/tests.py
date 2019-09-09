from django.test import TestCase
from django.apps import apps
from .apps import TodoConfig

# Create your tests here.
class TestDjango(TestCase):
    def test_django_is_created(self):
        self.assertEquals(1,1)
        
    def test_app_created(self):
        self.assertEqual("todo", TodoConfig.name)
        self.assertEqual("todo", apps.get_app_config("todo").name)