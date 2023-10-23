from django.test import TestCase, Client
from django.urls import reverse


class TestIndexViewCase(TestCase):

    client = Client()
    index_url = reverse('index')
    index_template = 'index.html'

    def test_booklist_view_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.index_template)