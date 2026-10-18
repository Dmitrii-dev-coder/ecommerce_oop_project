"""Тесты для абстрактного базового класса BaseProduct."""

import pytest
from abc import ABC

from src.base_product import BaseProduct
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


# ============================================================================
# 0. Проверка абстрактности класса BaseProduct
# ============================================================================


# Тест 001: Проверка что BaseProduct является абстрактным классом.
def test_base_product_is_abstract():
    """BaseProduct должен быть абстрактным классом."""
    assert issubclass(BaseProduct, ABC)


# Тест 002: Проверка что BaseProduct нельзя создать напрямую.
def test_base_product_cannot_be_instantiated():
    """Нельзя создать экземпляр абстрактного класса BaseProduct напрямую."""
    with pytest.raises(TypeError):
        BaseProduct(name="Тест", description="Описание", price=100.0, quantity=5)


# ============================================================================
# 1. Проверка наследования Product от BaseProduct
# ============================================================================


# Тест 101: Проверка что Product наследуется от BaseProduct.
def test_product_inherits_from_base_product():
    """Product должен наследоваться от BaseProduct."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert isinstance(product, BaseProduct)


# Тест 102: Проверка что Smartphone наследуется от BaseProduct.
def test_smartphone_inherits_from_base_product():
    """Smartphone должен наследоваться от BaseProduct через Product."""
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон Apple",
        price=99990.0,
        quantity=10,
        efficiency="high",
        model="iPhone 15 Pro",
        memory="256GB",
        color="Черный",
    )
    assert isinstance(smartphone, BaseProduct)


# Тест 103: Проверка что LawnGrass наследуется от BaseProduct.
def test_lawn_grass_inherits_from_base_product():
    """LawnGrass должен наследоваться от BaseProduct через Product."""
    lawn_grass = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert isinstance(lawn_grass, BaseProduct)


# ============================================================================
# 2. Проверка общей функциональности BaseProduct
# ============================================================================


# Тест 201: Проверка что new_product работает через Product.
def test_new_product_works():
    """Метод new_product должен создавать продукт из словаря."""
    product_data = {
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 100.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Тестовый товар"
    assert product.price == 100.0
    assert product.quantity == 10


# Тест 202: Проверка что __str__ работает через BaseProduct.
def test_str_works():
    """Метод __str__ должен возвращать строковое представление."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    result = str(product)
    assert "Товар" in result
    assert "100.0" in result
    assert "5" in result


# Тест 203: Проверка что __add__ работает через BaseProduct.
def test_add_works():
    """Метод __add__ должен складывать продукты одинакового типа."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert result == 110.0


# Тест 204: Проверка что __add__ вызывает TypeError для разных типов.
def test_add_raises_type_error():
    """Метод __add__ должен вызывать TypeError для разных типов."""
    product = Product(name="Товар", description="Описание", price=10.0, quantity=5)
    smartphone = Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон Apple",
        price=99990.0,
        quantity=10,
        efficiency="high",
        model="iPhone 15 Pro",
        memory="256GB",
        color="Черный",
    )
    with pytest.raises(TypeError):
        product + smartphone
