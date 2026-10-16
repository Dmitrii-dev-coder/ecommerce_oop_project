"""Конфигурация pytest — фикстуры для тестов."""

import pytest

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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


@pytest.fixture
def sample_smartphone():
    """Фикстура для Smartphone."""
    return Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон Apple",
        price=99990.0,
        quantity=10,
        efficiency="high",
        model="iPhone 15 Pro",
        memory="256GB",
        color="Черный",
    )


@pytest.fixture
def sample_lawn_grass():
    """Фикстура для LawnGrass."""
    return LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
