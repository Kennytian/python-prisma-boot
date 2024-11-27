from typing import List

from src.config.prisma_config import prisma
from src.schemas.product_schema import Product as ProductSchema, ProductCreate, ProductUpdate


class ProductService:
    async def get_products(self) -> List[ProductSchema]:
        # products = await prisma.product.find_many({
        #     "where": {
        #         "published": True
        #     }
        # })
        results = await prisma.product.find_many()
        return  [ProductSchema(**result.model_dump()) for result in results]

    async def get_product_by_id(self, id: str) -> ProductSchema:
        result = await prisma.product.find_unique({
            "where": {
                "id": id
            }
        })
        return ProductSchema(**result.model_dump())

    async def create_product(self, data: ProductCreate) -> ProductSchema:
        result = await prisma.product.create(data=data.model_dump())
        return ProductSchema(**result.model_dump())

    async def update_product(self, id: str, data: ProductUpdate) -> ProductSchema:
        result = await prisma.product.update(where={'id': id}, data=data.model_dump())
        return ProductSchema(**result.model_dump())

    async def delete_product(self, id: str ) -> ProductSchema:
        result = await prisma.product.delete(where={'id': id} )
        return ProductSchema(**result.model_dump())
