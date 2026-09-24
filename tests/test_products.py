import pytest


# ============================================================================
# 0. Проверка класса Products :
# ============================================================================

# Тест 001: Позитивный тест — проверка наличия атрибута name.

def test_product_has_name():
    """Product должен иметь атрибут name."""
    from src.products import Product

    product = Product(
        name="Тестовый товар",
        description="Описание",
        price=10.99,
        quantity=5
    )
    assert product.name is not None


# Тест 002: Позитивный тест — проверка наличия атрибута description.
def test_product_has_description():
    """Product должен иметь атрибут description."""
    from src.products import Product

    product = Product(
        name="Тестовый товар",
        description="Описание",
        price=10.99,
        quantity=5
    )
    assert product.description is not None


# Тест 003: Позитивный тест — проверка наличия атрибута price.
def test_product_has_price():
    """Product должен иметь атрибут price."""
    from src.products import Product

    product = Product(
        name="Тестовый товар",
        description="Описание",
        price=10.99,
        quantity=5
    )
    assert product.price is not None


# Тест 004: Позитивный тест — проверка наличия атрибута quantity.
def test_product_has_quantity():
    """Product должен иметь атрибут quantity."""
    from src.products import Product

    product = Product(
        name="Тестовый товар",
        description="Описание",
        price=10.99,
        quantity=5
    )
    assert product.quantity is not None