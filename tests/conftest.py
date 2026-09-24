"""Конфигурация pytest — фикстуры для тестов."""

import pytest

#from src.products import Product, Category

# @pytest.fixture
# def first_product():
#     """Фикстура для первого товара."""
#     return Product(
#         name="Первый товар",
#         description="Описание первого товара",
#         price=10.99,
#         quantity=5
#         )
#
#
# @pytest.fixture
# def first_category():
#     """Фикстура для первой категории."""
#     return Category(
#         name="Первая категория",
#         description="Описание первой категории",
#         products=[]
#     )

@pytest.fixture
def sample_product_data():
    """Данные для создания Product."""
    return {
        "name": "Тестовый товар",
        "description": "Тестовое описание",
        "price": 100.50,
        "quantity": 10
    }


@pytest.fixture
def sample_category_data():
    """Данные для создания Category."""
    return {
        "name": "Тестовая категория",
        "description": "Тестовое описание категории",
        "products": []
    }
