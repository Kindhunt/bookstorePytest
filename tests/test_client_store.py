import allure

from models.Cart import Cart, CartCreate, CartProduct
from models.Login import Login
from models.Product import Product, ProductCreate
from models.User import User, UserCreate


@allure.feature("Products")
@allure.title("Проверить что вернулся список продуктов")
def test_get_products(fake_store_client):
    response, products = fake_store_client.get_products()

    assert response.status_code == 200
    assert len(products) > 0
    assert all(isinstance(p, Product) for p in products)

@allure.feature("Products")
@allure.title("Проверить что вернулся продукт")
def test_get_product(fake_store_client):
    response, product = fake_store_client.get_product(17)

    assert response.status_code == 200
    assert isinstance(product, Product)
    assert product.id == 17

@allure.feature("Products")
@allure.title("Проверить, добавлен ли продукт")
def test_add_product(fake_store_client):
    new_product = ProductCreate(
        title="Bumbo adventure book",
        price=9.99,
        description="Book about elephant Bumbo and his friends adventures",
        category="kids book",
        image="https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2t.png"
    )

    response, product = fake_store_client.add_new_product(new_product)

    assert response.status_code == 201
    assert isinstance(product, Product)
    assert product.title == new_product.title

@allure.feature("Products")
@allure.title("Проверить, обновлён ли продукт")
def test_update_product(fake_store_client):
    new_product = ProductCreate(
        title="Totally Not Rain Jacket Women Windbreaker Striped Climbing Raincoats",
        price=59.99,
        description="Lightweight perfet for trip or casual wear ... it a real styled look.",
        category="women's clothing",
        image="https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2t.png"
    )

    response, product = fake_store_client.update_product(17, new_product)

    assert response.status_code == 200
    assert product.id == 17
    assert product.title == new_product.title
    assert product.price == new_product.price
    assert product.description == new_product.description

@allure.feature("Products")
@allure.title("Проверить удаление продукта")
def test_delete_product(fake_store_client):
    response = fake_store_client.delete_product(17)

    assert response.status_code == 200



@allure.feature("Carts")
@allure.title("Проверить что вернулся список корзин")
def test_get_carts(fake_store_client):
    response, carts = fake_store_client.get_carts()

    assert response.status_code == 200
    assert len(carts) > 0
    assert all(isinstance(c, Cart) for c in carts)

@allure.feature("Carts")
@allure.title("Проверить что вернулась корзина")
def test_get_cart(fake_store_client):
    response, cart = fake_store_client.get_cart(7)

    assert response.status_code == 200
    assert cart.id == 7
    assert len(cart.products) == 1

@allure.feature("Carts")
@allure.title("Проверить, добавлена ли корзина")
def test_add_cart(fake_store_client):
    new_cart = CartCreate(
        userId=4,
        products=[
            CartProduct(productId=17, quantity=2)
        ]
    )

    response, cart = fake_store_client.add_new_cart(new_cart)

    assert response.status_code == 201
    assert cart.userId == 4
    assert cart.products[0].productId == 17
    assert cart.products[0].quantity == 2

@allure.feature("Carts")
@allure.title("Проверить, обновлена ли корзина")
def test_update_cart(fake_store_client):
    new_cart = CartCreate(
        userId=4,
        products=[
            CartProduct(productId=17, quantity=2)
        ]
    )

    response, cart = fake_store_client.update_cart(7, new_cart)

    assert response.status_code == 200
    assert cart.id == 7
    assert cart.userId == new_cart.userId
    assert cart.products[0] == new_cart.products[0]

@allure.feature("Carts")
@allure.title("Проверить удаление корзины")
def test_delete_cart(fake_store_client):
    response = fake_store_client.delete_cart(7)

    assert response.status_code == 200



@allure.feature("Users")
@allure.title("Проверить что вернулся список пользователей")
def test_get_users(fake_store_client):
    response, users = fake_store_client.get_users()

    assert response.status_code == 200
    assert len(users) > 0
    assert all(isinstance(u, User) for u in users)

@allure.feature("Users")
@allure.title("Проверить что вернулся пользователь")
def test_get_user(fake_store_client):
    response, user = fake_store_client.get_user(1)

    assert response.status_code == 200
    assert user.id == 1
    assert user.username == "johnd"

@allure.feature("Users")
@allure.title("Проверить, добавлен ли пользователь")
def test_add_user(fake_store_client):
    new_user = UserCreate(
        username="user123",
        password="user123$",
        email="example@gmail.com"
    )

    response, user_id = fake_store_client.add_new_user(new_user)

    assert response.status_code == 201

@allure.feature("Users")
@allure.title("Проверить, обновлен ли пользователь")
def test_update_user(fake_store_client):
    new_user = UserCreate(
        username="user123",
        password="user123$",
        email="example@gmail.com"
    )

    response, user = fake_store_client.update_user(8, new_user)

    assert response.status_code == 200
    assert user.username == new_user.username
    assert user.password == new_user.password
    assert user.email == new_user.email

@allure.feature("Users")
@allure.title("Проверить удаление пользователя")
def test_delete_user(fake_store_client):
    response = fake_store_client.delete_user(1)

    assert response.status_code == 200



@allure.feature("Auth")
@allure.title("Проверить отдаётся ли JWT токен")
def test_auth(fake_store_client):
    credentials = Login(
        username="johnd",
        password="m38rmF$"
    )

    response, jwt_token = fake_store_client.login(credentials)

    assert response.status_code == 201
    assert jwt_token.token