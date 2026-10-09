"""Конфигурация pytest — фикстуры для тестов."""

import pytest

from src.product import Product
from src.category import Category


@pytest.fixture
def sample_product():
    """Фикстура для Product."""
    return Product(
        name="Тестовый товар",
        description="Тестовое описание",
        price=100.50,
        quantity=10,
    )


@pytest.fixture
def sample_category():
    """Фикстура для Category."""
    return Category(
        name="Тестовая категория",
        description="Тестовое описание",
        products=[],
    )
