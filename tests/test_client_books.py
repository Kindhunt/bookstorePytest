from clients.book_client import BooksClient


def test_get_books():
    client = BooksClient()

    response = client.get_books()

    assert response.status_code == 200