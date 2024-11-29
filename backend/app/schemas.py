from pydantic import BaseModel
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItem(OrderItemBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    user_id: int
    status: str

class Order(OrderBase):
    id: int
    items: List[OrderItem]

    class Config:
        orm_mode = True
