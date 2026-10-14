"""Тесты для класса Smartphone."""

from src.product import Product
from src.smartphone import Smartphone


# ============================================================================
# 0. Проверка наличия атрибутов name, description, price, quantity (наследование от Product)
# ============================================================================


# Тест 001: Позитивный тест — проверка наследования атрибута name.
def test_smartphone_inherits_name():
    """Smartphone должен наследовать атрибут name от Product."""
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
    assert smartphone.name == "iPhone 15"


# Тест 002: Позитивный тест — проверка наследования атрибута description.
def test_smartphone_inherits_description():
    """Smartphone должен наследовать атрибут description от Product."""
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
    assert smartphone.description == "Флагманский смартфон Apple"


# Тест 003: Позитивный тест — проверка наследования атрибута price.
def test_smartphone_inherits_price():
    """Smartphone должен наследовать атрибут price от Product."""
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
    assert smartphone.price == 99990.0


# Тест 004: Позитивный тест — проверка наследования атрибута quantity.
def test_smartphone_inherits_quantity():
    """Smartphone должен наследовать атрибут quantity от Product."""
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
    assert smartphone.quantity == 10


# ============================================================================
# 1. Проверка наличия новых атрибутов efficiency, model, memory, color
# ============================================================================


# Тест 101: Позитивный тест — проверка наличия атрибута efficiency.
def test_smartphone_has_efficiency():
    """Smartphone должен иметь атрибут efficiency."""
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
    assert smartphone.efficiency == "high"


# Тест 102: Позитивный тест — проверка наличия атрибута model.
def test_smartphone_has_model():
    """Smartphone должен иметь атрибут model."""
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
    assert smartphone.model == "iPhone 15 Pro"


# Тест 103: Позитивный тест — проверка наличия атрибута memory.
def test_smartphone_has_memory():
    """Smartphone должен иметь атрибут memory."""
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
    assert smartphone.memory == "256GB"


# Тест 104: Позитивный тест — проверка наличия атрибута color.
def test_smartphone_has_color():
    """Smartphone должен иметь атрибут color."""
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
    assert smartphone.color == "Черный"


# ============================================================================
# 2. Проверка магического метода __str__ для Smartphone
# ============================================================================


# Тест 201: Позитивный тест — __str__ для Smartphone возвращает строку.
def test_smartphone_str_returns_string():
    """Метод __str__ для Smartphone должен возвращать строку."""
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
    result = str(smartphone)
    assert isinstance(result, str)


# Тест 202: Позитивный тест — __str__ для Smartphone содержит название.
def test_smartphone_str_contains_name():
    """Метод __str__ для Smartphone должен содержать название."""
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
    result = str(smartphone)
    assert "iPhone 15" in result


# Тест 203: Позитивный тест — __str__ для Smartphone содержит модель.
def test_smartphone_str_contains_model():
    """Метод __str__ для Smartphone должен содержать модель."""
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
    result = str(smartphone)
    assert "iPhone 15 Pro" in result


# Тест 204: Позитивный тест — __str__ для Smartphone содержит цвет.
def test_smartphone_str_contains_color():
    """Метод __str__ для Smartphone должен содержать цвет."""
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
    result = str(smartphone)
    assert "Черный" in result


# ============================================================================
# 3. Проверка наследования от Product
# ============================================================================


# Тест 301: Позитивный тест — Smartphone является экземпляром Product.
def test_smartphone_is_instance_of_product():
    """Smartphone должен быть экземпляром Product."""
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
    assert isinstance(smartphone, Product)


# Тест 302: Позитивный тест — Smartphone является подклассом Product.
def test_smartphone_is_subclass_of_product():
    """Smartphone должен быть подклассом Product."""
    assert issubclass(Smartphone, Product)
