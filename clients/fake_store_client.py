from typing import List, Tuple

import requests
from requests import Response

from models.Cart import Cart, CartCreate
from models.Login import Login, JWTAuth
from models.Product import ProductCreate, Product
from models.User import User, UserCreate, UserId


class FakeStoreClient:

    BASE_URL = "https://fakestoreapi.com"

    def __init__(self):
        self.session = requests.session()

    def _parse_model(self, response: Response, model):
        return model.model_validate(response.json())

    def _parse_list(self, response: Response, model) -> List:
        return [model.model_validate(item) for item in response.json()]

    def get_products(self) -> Tuple[Response, List[Product]]:
        response = self.session.get(f"{self.BASE_URL}/products")
        return response, self._parse_list(response, Product)

    def add_new_product(self, product: ProductCreate) -> Tuple[Response, Product]:
        response = self.session.post(f"{self.BASE_URL}/products", json=product.model_dump())
        return response, self._parse_model(response, Product)

    def get_product(self, product_id: int) -> Tuple[Response, Product]:
        response = self.session.get(f"{self.BASE_URL}/products/{product_id}")
        return response, self._parse_model(response, Product)

    def update_product(self, product_id: int, product: ProductCreate) -> Tuple[Response, Product]:
        response = self.session.put(f"{self.BASE_URL}/products/{product_id}", json=product.model_dump())
        return response, self._parse_model(response, Product)

    def delete_product(self, product_id: int) -> Response:
        response = self.session.delete(f"{self.BASE_URL}/products/{product_id}")
        return response

    def get_carts(self) -> Tuple[Response, List[Cart]]:
        response = self.session.get(f"{self.BASE_URL}/carts")
        return response, self._parse_list(response, Cart)

    def add_new_cart(self, cart: CartCreate) -> Tuple[Response, Cart]:
        response = self.session.post(f"{self.BASE_URL}/carts", json=cart.model_dump())
        return response, self._parse_model(response, Cart)

    def get_cart(self, cart_id: int) -> Tuple[Response, Cart]:
        response = self.session.get(f"{self.BASE_URL}/carts/{cart_id}")
        return response, self._parse_model(response, Cart)

    def update_cart(self, cart_id: int, cart: CartCreate) -> Tuple[Response, Cart]:
        response = self.session.put(f"{self.BASE_URL}/carts/{cart_id}", json=cart.model_dump())
        return response, self._parse_model(response, Cart)

    def delete_cart(self, cart_id: int) -> Response:
        response = self.session.delete(f"{self.BASE_URL}/carts/{cart_id}")
        return response

    def get_users(self) -> Tuple[Response, List[User]]:
        response = self.session.get(f"{self.BASE_URL}/users")
        return response, self._parse_list(response, User)

    def add_new_user(self, user: UserCreate) -> Tuple[Response, UserId]:
        response = self.session.post(f"{self.BASE_URL}/users", json=user.model_dump())
        return response, self._parse_model(response, UserId)

    def get_user(self, user_id: int) -> Tuple[Response, User]:
        response = self.session.get(f"{self.BASE_URL}/users/{user_id}")
        return response, self._parse_model(response, User)

    def update_user(self, user_id: int, user: UserCreate) -> Tuple[Response, User]:
        response = self.session.put(f"{self.BASE_URL}/users/{user_id}", json=user.model_dump())
        return response, self._parse_model(response, User)

    def delete_user(self, user_id: int) -> Response:
        response = self.session.delete(f"{self.BASE_URL}/users/{user_id}")
        return response

    def login(self, credentials: Login) -> Tuple[Response, JWTAuth]:
        response = self.session.post(f"{self.BASE_URL}/auth/login", json=credentials.model_dump())
        return response, self._parse_model(response, JWTAuth)