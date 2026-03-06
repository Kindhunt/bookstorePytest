def test_get_books(books_client):
    response = books_client.get_books()
    assert response.status_code == 200