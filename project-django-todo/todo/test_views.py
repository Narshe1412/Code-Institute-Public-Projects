from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item

# Create your tests here.
class TestViews(TestCase):
    
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "todo_list.html")
        
    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_item_page(self):
        item = Item(name='Test Edit Page')
        item.save()
        
        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")
        
    def test_get_edit_item_page_for_unexisting_item(self):
        page = self.client.get("/edit/12331")
        self.assertEqual(page.status_code, 404)
    
    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)
        
    def test_post_edit_an_item(self):
        item = Item(name="Create one")
        item.save()
        id= item.id
        
        request= self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create one")
        item.save()
        id= item.id
        
        request= self.client.post("/toggle/{0}".format(id))
        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
