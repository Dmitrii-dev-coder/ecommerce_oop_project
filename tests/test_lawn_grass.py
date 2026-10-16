"""Тесты для класса LawnGrass."""

from src.product import Product


# ============================================================================
# 0. Проверка наличия атрибутов name, description, price, quantity у экземпляра класса LawnGrass
# (наследование от Product)
# ============================================================================


# Тест 001: Позитивный тест — проверка наследования атрибута name.
def test_lawn_grass_inherits_name(sample_lawn_grass):
    """LawnGrass должен наследовать атрибут name от Product."""
    assert sample_lawn_grass.name == "Газонный травяной mix"


# Тест 002: Позитивный тест — проверка наследования атрибута description.
def test_lawn_grass_inherits_description(sample_lawn_grass):
    """LawnGrass должен наследовать атрибут description от Product."""
    assert sample_lawn_grass.description == "Смесь газонных трав"


# Тест 003: Позитивный тест — проверка наследования атрибута price.
def test_lawn_grass_inherits_price(sample_lawn_grass):
    """LawnGrass должен наследовать атрибут price от Product."""
    assert sample_lawn_grass.price == 500.0


# Тест 004: Позитивный тест — проверка наследования атрибута quantity.
def test_lawn_grass_inherits_quantity(sample_lawn_grass):
    """LawnGrass должен наследовать атрибут quantity от Product."""
    assert sample_lawn_grass.quantity == 20


# ============================================================================
# 1. Проверка наличия новых атрибутов country, germination_period, color
# ============================================================================


# Тест 101: Позитивный тест — проверка наличия атрибута country.
def test_lawn_grass_has_country(sample_lawn_grass):
    """LawnGrass должен иметь атрибут country."""
    assert sample_lawn_grass.country == "Россия"


# Тест 102: Позитивный тест — проверка наличия атрибута germination_period.
def test_lawn_grass_has_germination_period(sample_lawn_grass):
    """LawnGrass должен иметь атрибут germination_period."""
    assert sample_lawn_grass.germination_period == "14 дней"


# Тест 103: Позитивный тест — проверка наличия атрибута color.
def test_lawn_grass_has_color(sample_lawn_grass):
    """LawnGrass должен иметь атрибут color."""
    assert sample_lawn_grass.color == "Зеленый"


# ============================================================================
# 2. Проверка магического метода __str__ для LawnGrass
# ============================================================================


# Тест 201: Позитивный тест — __str__ для LawnGrass возвращает строку.
def test_lawn_grass_str_returns_string(sample_lawn_grass):
    """Метод __str__ для LawnGrass должен возвращать строку."""
    result = str(sample_lawn_grass)
    assert isinstance(result, str)


# Тест 202: Позитивный тест — __str__ для LawnGrass содержит название.
def test_lawn_grass_str_contains_name(sample_lawn_grass):
    """Метод __str__ для LawnGrass должен содержать название."""
    result = str(sample_lawn_grass)
    assert "Газонный травяной mix" in result


# Тест 203: Позитивный тест — __str__ для LawnGrass содержит страну.
def test_lawn_grass_str_contains_country(sample_lawn_grass):
    """Метод __str__ для LawnGrass должен содержать страну."""
    result = str(sample_lawn_grass)
    assert "Россия" in result


# Тест 204: Позитивный тест — __str__ для LawnGrass содержит цвет.
def test_lawn_grass_str_contains_color(sample_lawn_grass):
    """Метод __str__ для LawnGrass должен содержать цвет."""
    result = str(sample_lawn_grass)
    assert "Зеленый" in result


# ============================================================================
# 3. Проверка отношений наследования экземпляров класса LawnGrass через isinstance/issubclass от класса Product
# ============================================================================


# Тест 301: Позитивный тест — LawnGrass является экземпляром Product.
def test_lawn_grass_is_instance_of_product(sample_lawn_grass):
    """LawnGrass должен быть экземпляром Product."""
    assert isinstance(sample_lawn_grass, Product)


# Тест 302: Позитивный тест — LawnGrass является подклассом Product.
def test_lawn_grass_is_subclass_of_product():
    """LawnGrass должен быть подклассом Product."""
    from src.lawn_grass import LawnGrass
    assert issubclass(LawnGrass, Product)
