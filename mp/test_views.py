from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import Item


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "mp_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item = Item(name="Create A Test")
        item.save()

        page = self.client.get("/edit/{0}".format(item.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_for_page_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    def test_post_create_an_item(self):
        self.client.post("/add", {"name": "Create a Test"})
        item = get_object_or_404(Item, pk=1)
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name="Create A Test")
        item.save()
        id = item.id

        self.client.post("/edit/{0}".format(id), {"name": "A Different Name"})
        item = get_object_or_404(Item, pk=id)
        self.assertEqual("A Different Name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create A Test")
        item.save()
        id = item.id

        self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
