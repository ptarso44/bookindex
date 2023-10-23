from django.test import TestCase
from django.core.paginator import Paginator


class TestBookPaginationCase(TestCase):

    paginator_10_pages = Paginator('a'*40, 4)

    def test_pagination_when_page_at_the_middle(self):

        paginator_20_pages = Paginator('a'*80, 4)

        page_numbers = paginator_20_pages.get_elided_page_range(11, on_each_side=2, on_ends=2)
        page_list = [i for i in page_numbers]

        self.assertEqual(list(page_list), [1, 2, '…', 9, 10, 11, 12, 13, '…', 19, 20])

    def test_pagination_when_current_page_close_to_beginning(self):

        page_numbers = self.paginator_10_pages.get_elided_page_range(2, on_each_side=1, on_ends=3)
        page_list = [i for i in page_numbers]
        self.assertEqual(list(page_list), [1, 2, 3, '…', 8, 9, 10])

    def test_pagination_when_current_page_close_to_end(self):

        page_numbers = self.paginator_10_pages.get_elided_page_range(8, on_each_side=2, on_ends=2)
        page_list = [i for i in page_numbers]
        self.assertEqual(list(page_list), [1, 2, '…', 6, 7, 8, 9, 10])

    def test_pagination_when_zero_boundaries_and_around(self):

        page_numbers = self.paginator_10_pages.get_elided_page_range(5, on_each_side=0, on_ends=0)
        page_list = [i for i in page_numbers]
        self.assertEqual(list(page_list), ['…', 5, '…'])
