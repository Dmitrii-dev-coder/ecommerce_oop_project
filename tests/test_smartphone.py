"""Тесты для класса Smartphone."""

from src.product import Product


# ============================================================================
# 0. Проверка наличия атрибутов name, description, price, quantity (наследование от Product)
# ============================================================================


# Тест 001: Позитивный тест — проверка наследования атрибута name.
def test_smartphone_inherits_name(sample_smartphone):
    """Smartphone должен наследовать атрибут name от Product."""
    assert sample_smartphone.name == "iPhone 15"


# Тест 002: Позитивный тест — проверка наследования атрибута description.
def test_smartphone_inherits_description(sample_smartphone):
    """Smartphone должен наследовать атрибут description от Product."""
    assert sample_smartphone.description == "Флагманский смартфон Apple"


# Тест 003: Позитивный тест — проверка наследования атрибута price.
def test_smartphone_inherits_price(sample_smartphone):
    """Smartphone должен наследовать атрибут price от Product."""
    assert sample_smartphone.price == 99990.0


# Тест 004: Позитивный тест — проверка наследования атрибута quantity.
def test_smartphone_inherits_quantity(sample_smartphone):
    """Smartphone должен наследовать атрибут quantity от Product."""
    assert sample_smartphone.quantity == 10


# ============================================================================
# 1. Проверка наличия новых атрибутов efficiency, model, memory, color
# ============================================================================


# Тест 101: Позитивный тест — проверка наличия атрибута efficiency.
def test_smartphone_has_efficiency(sample_smartphone):
    """Smartphone должен иметь атрибут efficiency."""
    assert sample_smartphone.efficiency == "high"


# Тест 102: Позитивный тест — проверка наличия атрибута model.
def test_smartphone_has_model(sample_smartphone):
    """Smartphone должен иметь атрибут model."""
    assert sample_smartphone.model == "iPhone 15 Pro"


# Тест 103: Позитивный тест — проверка наличия атрибута memory.
def test_smartphone_has_memory(sample_smartphone):
    """Smartphone должен иметь атрибут memory."""
    assert sample_smartphone.memory == "256GB"


# Тест 104: Позитивный тест — проверка наличия атрибута color.
def test_smartphone_has_color(sample_smartphone):
    """Smartphone должен иметь атрибут color."""
    assert sample_smartphone.color == "Черный"


# ============================================================================
# 2. Проверка магического метода __str__ для Smartphone
# ============================================================================


# Тест 201: Позитивный тест — __str__ для Smartphone возвращает строку.
def test_smartphone_str_returns_string(sample_smartphone):
    """Метод __str__ для Smartphone должен возвращать строку."""
    result = str(sample_smartphone)
    assert isinstance(result, str)


# Тест 202: Позитивный тест — __str__ для Smartphone содержит название.
def test_smartphone_str_contains_name(sample_smartphone):
    """Метод __str__ для Smartphone должен содержать название."""
    result = str(sample_smartphone)
    assert "iPhone 15" in result


# Тест 203: Позитивный тест — __str__ для Smartphone содержит модель.
def test_smartphone_str_contains_model(sample_smartphone):
    """Метод __str__ для Smartphone должен содержать модель."""
    result = str(sample_smartphone)
    assert "iPhone 15 Pro" in result


# Тест 204: Позитивный тест — __str__ для Smartphone содержит цвет.
def test_smartphone_str_contains_color(sample_smartphone):
    """Метод __str__ для Smartphone должен содержать цвет."""
    result = str(sample_smartphone)
    assert "Черный" in result


# ============================================================================
# 3. Проверка наследования от Product
# ============================================================================


# Тест 301: Позитивный тест — Smartphone является экземпляром Product.
def test_smartphone_is_instance_of_product(sample_smartphone):
    """Smartphone должен быть экземпляром Product."""
    assert isinstance(sample_smartphone, Product)


# Тест 302: Позитивный тест — Smartphone является подклассом Product.
def test_smartphone_is_subclass_of_product():
    """Smartphone должен быть подклассом Product."""
    from src.smartphone import Smartphone
    assert issubclass(Smartphone, Product)
