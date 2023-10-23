from django.test import TestCase, Client
from django.urls import reverse


class BookListViewTestCase(TestCase):

    client = Client()
    booklist_url = reverse('booklist')
    booklist_template = 'books/book_list.html'

    def test_booklist_view_GET(self):
        response = self.client.get(self.booklist_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.booklist_template)
