from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    title: str
    category: str
    price: float
    description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: Optional[str] = None

    class Config:
        from_attributes = True
