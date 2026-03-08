from typing import List

from pydantic import BaseModel

from models.Product import Product


class CartProduct(BaseModel):
    id: int

class CartCreate(BaseModel):
    userId: int
    products: List[CartProduct]

class Cart(BaseModel):
    id: int
    userId: int
    products: List[Product]