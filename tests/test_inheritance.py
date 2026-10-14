"""Тесты для ограничений сложения (__add__) и добавления продуктов (add_product)."""

import pytest

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


# ============================================================================
# 0. Тесты для __add__ с ограничениями типа (Задание 2)
# ============================================================================


# Тест 001: Позитивный тест — сложение двух Product работает.
def test_add_two_product():
    """Сложение двух Product объектов должно работать."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert result == 110.0


# Тест 002: Позитивный тест — сложение двух Smartphone работает.
def test_add_two_smartphone():
    """Сложение двух Smartphone объектов должно работать."""
    smartphone1 = Smartphone(
        name="iPhone 15",
        description="Флагманский смартфон Apple",
        price=99990.0,
        quantity=10,
        efficiency="high",
        model="iPhone 15 Pro",
        memory="256GB",
        color="Черный",
    )
    smartphone2 = Smartphone(
        name="Samsung Galaxy",
        description="Флагманский смартфон Samsung",
        price=89990.0,
        quantity=5,
        efficiency="high",
        model="Galaxy S24",
        memory="128GB",
        color="Белый",
    )
    result = smartphone1 + smartphone2
    assert isinstance(result, float)
    assert result > 0


# Тест 003: Позитивный тест — сложение двух LawnGrass работает.
def test_add_two_lawn_grass():
    """Сложение двух LawnGrass объектов должно работать."""
    lawn_grass1 = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    lawn_grass2 = LawnGrass(
        name="Газон 2",
        description="Смесь газонных трав",
        price=600.0,
        quantity=15,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    result = lawn_grass1 + lawn_grass2
    assert isinstance(result, float)
    assert result > 0


# Тест 004: Негативный тест — сложение Smartphone и LawnGrass вызывает TypeError.
def test_add_smartphone_and_lawn_grass_raises_type_error():
    """Сложение Smartphone и LawnGrass должно вызывать TypeError."""
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
    lawn_grass = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    with pytest.raises(TypeError) as exc_info:
        smartphone + lawn_grass
    assert "одного класса" in str(exc_info.value)


# Тест 005: Негативный тест — сложение Smartphone и Product вызывает TypeError.
def test_add_smartphone_and_product_raises_type_error():
    """Сложение Smartphone и Product должно вызывать TypeError."""
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
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with pytest.raises(TypeError) as exc_info:
        smartphone + product
    assert "одного класса" in str(exc_info.value)


# Тест 006: Негативный тест — сложение LawnGrass и Product вызывает TypeError.
def test_add_lawn_grass_and_product_raises_type_error():
    """Сложение LawnGrass и Product должно вызывать TypeError."""
    lawn_grass = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with pytest.raises(TypeError) as exc_info:
        lawn_grass + product
    assert "одного класса" in str(exc_info.value)


# Тест 007: Негативный тест — сложение Product со строкой вызывает TypeError.
def test_add_product_and_string_raises_type_error():
    """Сложение Product и строки должно вызывать TypeError."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with pytest.raises(TypeError) as exc_info:
        product + "не продукт"
    assert "одного класса" in str(exc_info.value)


# ============================================================================
# 1. Тесты для add_product с ограничениями типа (Задание 3)
# ============================================================================


# Тест 101: Позитивный тест — добавление Product в категорию работает.
def test_add_product_to_category():
    """Добавление Product в категорию должно работать."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)

    category.add_product(product)
    assert len(category.products_list) == 1
    assert category.products_list[0] is product


# Тест 102: Позитивный тест — добавление Smartphone в категорию работает.
def test_add_smartphone_to_category():
    """Добавление Smartphone в категорию должно работать."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
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

    category.add_product(smartphone)
    assert len(category.products_list) == 1
    assert category.products_list[0] is smartphone


# Тест 103: Позитивный тест — добавление LawnGrass в категорию работает.
def test_add_lawn_grass_to_category():
    """Добавление LawnGrass в категорию должно работать."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    lawn_grass = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )

    category.add_product(lawn_grass)
    assert len(category.products_list) == 1
    assert category.products_list[0] is lawn_grass


# Тест 104: Негативный тест — добавление строки в категорию вызывает TypeError.
def test_add_string_to_category_raises_type_error():
    """Добавление строки в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product("не продукт")
    assert "Product" in str(exc_info.value) or "продукт" in str(exc_info.value).lower()


# Тест 105: Негативный тест — добавление числа в категорию вызывает TypeError.
def test_add_int_to_category_raises_type_error():
    """Добавление числа в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product(123)
    assert "Product" in str(exc_info.value) or "продукт" in str(exc_info.value).lower()


# Тест 106: Негативный тест — добавление None в категорию вызывает TypeError.
def test_add_none_to_category_raises_type_error():
    """Добавление None в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product(None)
    assert "Product" in str(exc_info.value) or "продукт" in str(exc_info.value).lower()


# Тест 107: Негативный тест — добавление словаря в категорию вызывает TypeError.
def test_add_dict_to_category_raises_type_error():
    """Добавление словаря в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product({"name": "Товар"})
    assert "Product" in str(exc_info.value) or "продукт" in str(exc_info.value).lower()
