"""Тесты для класса-миксина PrintInfoMixin."""

import unittest.mock
from io import StringIO

from src.mixin import PrintInfoMixin
from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


# ============================================================================
# 0. Проверка наличия миксина в Product
# ============================================================================


# Тест 001: Проверка, что Product содержит PrintInfoMixin в MRO.
def test_product_has_mixin_in_mro():
    """Product должен содержать PrintInfoMixin в цепочке наследования."""
    assert PrintInfoMixin in Product.__mro__


# ============================================================================
# 1. Проверка печати информации при создании объекта
# ============================================================================


# Тест 101: Проверка, что при создании экземпляра Product печатается информация.
def test_product_prints_creation_info():
    """При создании экземпляра Product должна печататься информация о создании."""
    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        _ = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    output = mock_stdout.getvalue()
    assert "Товар" in output
    assert "100.0" in output
    assert "5" in output


# Тест 102: Проверка, что при создании Smartphone печатается информация.
def test_smartphone_prints_creation_info():
    """При создании Smartphone должна печататься информация о создании."""
    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        _ = Smartphone(
            name="iPhone 15",
            description="Флагманский смартфон Apple",
            price=99990.0,
            quantity=10,
            efficiency="high",
            model="iPhone 15 Pro",
            memory="256GB",
            color="Черный",
        )
        output = mock_stdout.getvalue()
        assert "Smartphone" in output
        assert "iPhone 15" in output
        assert "99990.0" in output
        assert "10" in output


# Тест 103: Проверка, что при создании LawnGrass печатается информация.
def test_lawn_grass_prints_creation_info():
    """При создании LawnGrass должна печататься информация о создании."""
    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        _ = LawnGrass(
            name="Газон 1",
            description="Смесь газонных трав",
            price=500.0,
            quantity=20,
            country="Россия",
            germination_period="14 дней",
            color="Зеленый",
        )
        output = mock_stdout.getvalue()
        assert "LawnGrass" in output
        assert "Газон 1" in output
        assert "500.0" in output
        assert "20" in output


# ============================================================================
# 2. Проверка корректности формата вывода
# ============================================================================


# Тест 201: Проверка, что вывод содержит все параметры.
def test_print_info_contains_all_params():
    """Вывод информации о создании должен содержать все параметры."""
    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        _ = Product(name="Тест", description="Описание", price=150.0, quantity=7)
        output = mock_stdout.getvalue()
        assert "Тест" in output
        assert "Описание" in output
        assert "150.0" in output
        assert "7" in output


# Тест 202: Проверка, что миксин не ломает наследование.
def test_mixin_does_not_break_inheritance():
    """Миксин не должен ломать цепочку наследования."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert isinstance(product, Product)
    assert isinstance(product, PrintInfoMixin)
