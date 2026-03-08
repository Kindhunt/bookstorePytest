from pydantic import BaseModel


class ProductCreate(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str

class Product(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str