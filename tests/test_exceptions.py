"""Тесты для дополнительного задания — пользовательское исключение ZeroQuantityError."""

import pytest
from io import StringIO
import unittest.mock

from src.product import Product
from src.category import Category
from src.exceptions import ZeroQuantityError


# ============================================================================
# 0. Проверка класса ZeroQuantityError
# ============================================================================


# Тест 001: Проверка что ZeroQuantityError является подклассом Exception.
def test_zero_quantity_error_is_exception():
    """ZeroQuantityError должен быть подклассом Exception."""
    assert issubclass(ZeroQuantityError, Exception)


# Тест 002: Проверка что ZeroQuantityError выбрасывается с сообщением.
def test_zero_quantity_error_has_message():
    """ZeroQuantityError должен содержать сообщение."""
    with pytest.raises(ZeroQuantityError) as exc_info:
        raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен")
    assert "нулевым количеством" in str(exc_info.value)


# ============================================================================
# 1. Проверка использования ZeroQuantityError в Category.add_product
# ============================================================================


# Тест 101: Проверка что add_product использует try/except/else/finally.
def test_add_product_uses_try_except_else_finally():
    """Метод add_product должен использовать блоки try/except/else/finally."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)

    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        category.add_product(product)
    output = mock_stdout.getvalue()
    assert "Товар добавлен" in output
    assert "Обработка добавления товара завершена" in output


# Тест 102: Проверка что при успешном добавлении выводится «Товар добавлен».
def test_add_product_success_message():
    """При успешном добавлении товара должно выводиться сообщение «Товар добавлен»."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)

    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        category.add_product(product)
    output = mock_stdout.getvalue()
    assert "Товар добавлен" in output


# Тест 103: Проверка что «Обработка добавления товара завершена» выводится всегда.
def test_add_product_finally_message_always():
    """Сообщение «Обработка добавления товара завершена» должно выводиться при любом исходе."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)

    with unittest.mock.patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        category.add_product(product)
    output = mock_stdout.getvalue()
    assert "Обработка добавления товара завершена" in output
