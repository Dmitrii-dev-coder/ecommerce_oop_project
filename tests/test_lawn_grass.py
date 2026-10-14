"""Тесты для класса LawnGrass."""

from src.product import Product
from src.lawn_grass import LawnGrass


# ============================================================================
# 0. Проверка наличия атрибутов name, description, price, quantity (наследование от Product)
# ============================================================================


# Тест 001: Позитивный тест — проверка наследования атрибута name.
def test_lawn_grass_inherits_name():
    """LawnGrass должен наследовать атрибут name от Product."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.name == "Газонный травяной mix"


# Тест 002: Позитивный тест — проверка наследования атрибута description.
def test_lawn_grass_inherits_description():
    """LawnGrass должен наследовать атрибут description от Product."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.description == "Смесь газонных трав"


# Тест 003: Позитивный тест — проверка наследования атрибута price.
def test_lawn_grass_inherits_price():
    """LawnGrass должен наследовать атрибут price от Product."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.price == 500.0


# Тест 004: Позитивный тест — проверка наследования атрибута quantity.
def test_lawn_grass_inherits_quantity():
    """LawnGrass должен наследовать атрибут quantity от Product."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.quantity == 20


# ============================================================================
# 1. Проверка наличия новых атрибутов country, germination_period, color
# ============================================================================


# Тест 101: Позитивный тест — проверка наличия атрибута country.
def test_lawn_grass_has_country():
    """LawnGrass должен иметь атрибут country."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.country == "Россия"


# Тест 102: Позитивный тест — проверка наличия атрибута germination_period.
def test_lawn_grass_has_germination_period():
    """LawnGrass должен иметь атрибут germination_period."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.germination_period == "14 дней"


# Тест 103: Позитивный тест — проверка наличия атрибута color.
def test_lawn_grass_has_color():
    """LawnGrass должен иметь атрибут color."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.color == "Зеленый"


# ============================================================================
# 2. Проверка магического метода __str__ для LawnGrass
# ============================================================================


# Тест 201: Позитивный тест — __str__ для LawnGrass возвращает строку.
def test_lawn_grass_str_returns_string():
    """Метод __str__ для LawnGrass должен возвращать строку."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    result = str(lawn_grass)
    assert isinstance(result, str)


# Тест 202: Позитивный тест — __str__ для LawnGrass содержит название.
def test_lawn_grass_str_contains_name():
    """Метод __str__ для LawnGrass должен содержать название."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    result = str(lawn_grass)
    assert "Газонный травяной mix" in result


# Тест 203: Позитивный тест — __str__ для LawnGrass содержит страну.
def test_lawn_grass_str_contains_country():
    """Метод __str__ для LawnGrass должен содержать страну."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    result = str(lawn_grass)
    assert "Россия" in result


# Тест 204: Позитивный тест — __str__ для LawnGrass содержит цвет.
def test_lawn_grass_str_contains_color():
    """Метод __str__ для LawnGrass должен содержать цвет."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    result = str(lawn_grass)
    assert "Зеленый" in result


# ============================================================================
# 3. Проверка наследования от Product
# ============================================================================


# Тест 301: Позитивный тест — LawnGrass является экземпляром Product.
def test_lawn_grass_is_instance_of_product():
    """LawnGrass должен быть экземпляром Product."""
    lawn_grass = LawnGrass(
        name="Газонный травяной mix",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert isinstance(lawn_grass, Product)


# Тест 302: Позитивный тест — LawnGrass является подклассом Product.
def test_lawn_grass_is_subclass_of_product():
    """LawnGrass должен быть подклассом Product."""
    assert issubclass(LawnGrass, Product)
