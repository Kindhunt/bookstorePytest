import pytest

from clients.fake_store_client import BooksClient


@pytest.fixture
def books_client():
    return BooksClient()