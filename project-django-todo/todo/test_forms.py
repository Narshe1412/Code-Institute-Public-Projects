from django.test import TestCase
from .forms import ItemForm

# Create your tests here.
class TestToDoItemFOrm(TestCase):
    
    def test_can_create_an_item_with_just_a_name(self):
        form = ItemForm({'name': 'Create tests'})    
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_an_item_without_a_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        