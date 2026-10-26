"""Тесты для абстрактного базового класса BaseProduct."""

import pytest
from abc import ABC

from src.base_product import BaseProduct
from src.product import Product


# ============================================================================
# 0. Проверка абстрактности класса BaseProduct
# ============================================================================


# Тест 001: Проверка, что BaseProduct является абстрактным классом.
def test_base_product_is_abstract():
    """BaseProduct должен быть абстрактным классом."""
    assert issubclass(BaseProduct, ABC)


# Тест 002: Проверка, что из BaseProduct нельзя создать экземпляр напрямую.
def test_base_product_cannot_be_instantiated():
    """Нельзя создать экземпляр абстрактного класса BaseProduct напрямую."""
    with pytest.raises(TypeError):
        BaseProduct(name="Тест", description="Описание", price=100.0, quantity=5)


# ============================================================================
# 1. Проверка наследования Product от BaseProduct
# ============================================================================


# Тест 101: Проверка, что Product наследуется от BaseProduct.
def test_product_inherits_from_base_product():
    """Product должен наследоваться от BaseProduct."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert isinstance(product, BaseProduct)


# Тест 102: Проверка, что Smartphone наследуется от BaseProduct.
def test_smartphone_inherits_from_base_product(sample_smartphone):
    """Smartphone должен наследоваться от BaseProduct через Product."""
    assert isinstance(sample_smartphone, BaseProduct)


# Тест 103: Проверка, что LawnGrass наследуется от BaseProduct.
def test_lawn_grass_inherits_from_base_product(sample_lawn_grass):
    """LawnGrass должен наследоваться от BaseProduct через Product."""
    assert isinstance(sample_lawn_grass, BaseProduct)


# ============================================================================
# 2. Проверка общей функциональности BaseProduct
# ============================================================================


# Тест 201: Проверка, что new_product работает через Product.
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


# Тест 202: Проверка, что __str__ возвращает строковое представление.
def test_str_works(sample_product):
    """Метод __str__ должен возвращать строковое представление."""
    result = str(sample_product)
    assert "Тестовый товар" in result
    assert "100.5" in result
    assert "10" in result


# Тест 203: Проверка, что __add__ работает для одинаковых типов.
def test_add_works():
    """Метод __add__ должен складывать продукты одинакового типа."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert result == 110.0


# Тест 204: Проверка, что __add__ вызывает TypeError для разных типов.
def test_add_raises_type_error(sample_product, sample_smartphone):
    """Метод __add__ должен вызывать TypeError для разных типов."""
    with pytest.raises(TypeError):
        sample_product + sample_smartphone
