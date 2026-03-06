import pytest

from clients.book_client import BooksClient


@pytest.fixture
def books_client():
    return BooksClient()