from fastapi import APIRouter, Depends, HTTPException, status

from typing import List

from src.services.product_service import ProductService

from src.schemas.product_schema import Product, ProductCreate

import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get('api/products', response_model=List[Product], status_code=status.HTTP_200_OK)
async def get_products(product_service: ProductService = Depends()):
    """
    Get all products
    """
    results = await product_service.get_products()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not available")
    return results


@router.post('api/product', response_model=ProductCreate, status_code=status.HTTP_201_CREATED)
async def create_product(data: ProductCreate, product_service: ProductService = Depends()):
    """
    Create a product
    """
    result = await product_service.create_product(data)
    logger.info(f'Product created: {result}')
    return result
