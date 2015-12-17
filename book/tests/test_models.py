import pytest
from ..models import Book
# from django.test import TestCase
from decimal import Decimal

"""
class BookModelTestCase(TestCase):
    def setUp(self):
        book_data = {
            'title': 'meetup 12 2015',
            'isbn': '1112223334445',
            'value': Decimal('132.23')
        }
        self.book = Book.objects.create(**book_data)

    def test_unicode(self):
        self.assertEquals(self.book.__unicode__(),
                          "The book {} costs: {}".format(
                              "meetup 12 2015", Decimal('132.23')))
"""
pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_book():
    book_data = {
        'title': 'meetup 12 2015',
        'isbn': '1112223334445',
        'value': Decimal('132.23')
    }
    return Book.objects.create(**book_data)


def test_unicode(create_book):
    book = create_book
    assert book.__unicode__() == "The book {} costs: {}".format(
        "meetup 12 2015", Decimal('132.23'))
