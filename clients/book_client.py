import requests


class BooksClient:

    BASE_URL = "https://demoqa.com/BookStore/v1"

    def get_books(self):
        return requests.get(f"{self.BASE_URL}/Books")

    def create_book(self, data):
        return requests.post(
            f"{self.BASE_URL}/Books",
            json=data
        )