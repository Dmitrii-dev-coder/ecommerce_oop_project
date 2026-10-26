"""Тесты для класса Category."""

import pytest

from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


# ============================================================================
# 0. Проверка атрибутов name, description, __products, category_count, product_count в Category
# ============================================================================


# Тест 001: Позитивный тест — проверка наличия атрибута name.
def test_category_has_name(sample_category):
    """Category должен иметь атрибут name."""
    assert sample_category.name is not None


# Тест 002: Позитивный тест — проверка наличия атрибута description.
def test_category_has_description(sample_category):
    """Category должен иметь атрибут description."""
    assert sample_category.description is not None


# Тест 003: Позитивный тест — проверка наличия приватного атрибута __products.
def test_category_has_products_list(sample_category):
    """Category должен иметь приватный атрибут __products типа list."""
    products = sample_category.products_list
    assert isinstance(products, list)


# Тест 004: Позитивный тест — проверка наличия атрибута category_count.
def test_category_count_increments():
    """Category.category_count должен увеличиваться."""
    Category.category_count = 0
    Category.product_count = 0

    Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    assert Category.category_count == 1


# Тест 005: Позитивный тест — проверка наличия атрибута product_count.
def test_product_count_increments():
    """Category.product_count должен увеличиваться на количество товаров."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product(name="Товар 1", description="Описание", price=10.99, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.99, quantity=3)
    product3 = Product(name="Товар 3", description="Описание", price=30.99, quantity=1)

    Category(
        name="Тестовая категория",
        description="Описание",
        products=[product1, product2, product3],
    )
    assert Category.product_count == 3


# ============================================================================
# 1. Проверка метода add_product для добавления продукта в __products и product_count в Category
# ============================================================================


# Тест 101: Позитивный тест — add_product добавляет продукт в список.
def test_add_product_appends_to_list():
    """Метод add_product должен добавлять продукт в __products."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=10.99, quantity=5)

    category.add_product(product)
    products = category.products_list
    assert len(products) == 1
    assert products[0] is product


# Тест 102: Позитивный тест — add_product увеличивает product_count.
def test_add_product_increments_product_count():
    """Метод add_product должен увеличивать Category.product_count."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=10.99, quantity=5)

    category.add_product(product)
    assert Category.product_count == 1


# Тест 103: Позитивный тест — add_product возвращает None.
def test_add_product_returns_none():
    """Метод add_product не должен возвращать значений."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=10.99, quantity=5)

    result = category.add_product(product)
    assert result is None


# Тест 104: Позитивный тест — геттер products возвращает строку с корректными данными.
def test_products_getter_returns_string():
    """Геттер products должен возвращать строку и содержать название, цену и количество продукта."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=10.99, quantity=5)
    category.add_product(product)

    result = category.products
    assert isinstance(result, str)
    assert "Товар" in result
    assert "10.99" in result
    assert "5" in result


# Тест 105: Позитивный тест — геттер products имеет правильный формат.
def test_products_getter_format():
    """Геттер products должен возвращать строку в формате: Название, X руб. Остаток: X шт."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product = Product(name="Товар", description="Описание", price=10.99, quantity=5)
    category.add_product(product)

    result = category.products
    assert "Товар, 10.99 руб. Остаток: 5 шт." in result


# Тест 106: Позитивный тест — геттер products с несколькими товарами.
def test_products_getter_multiple_products():
    """Геттер products должен корректно отображать несколько товаров."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[],
    )
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=10)
    category.add_product(product1)
    category.add_product(product2)

    result = category.products
    assert "Товар 1" in result
    assert "Товар 2" in result
    assert "10.0" in result
    assert "20.0" in result


# ============================================================================
# 2. Проверка магического метода __str__ для Category
# ============================================================================


# Тест 201: Позитивный тест — __str__ для Category возвращает строку.
def test_category_str_returns_string():
    """Метод __str__ для Category должен возвращать строку в формате: Название, количество продуктов: X шт."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Электроника",
        description="Техника и гаджеты",
        products=[],
    )
    result = str(category)
    assert isinstance(result, str)
    assert "Электроника" in result
    assert "количество продуктов" in result
    assert "0" in result


# Тест 202: Позитивный тест — __str__ для Category показывает сумму quantity.
def test_category_str_with_products():
    """Метод __str__ для Category должен показывать сумму quantity всех продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=10)
    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[product1, product2],
    )
    result = str(category)
    assert "количество продуктов" in result
    assert "15" in result


# ============================================================================
# 3. Проверка ограничений добавления продукта через isinstance()
# ============================================================================


# Тест 301: Позитивный тест — добавление экземпляра Product в категорию работает.
def test_add_product_to_category():
    """Добавление Product Объекта в категорию должно работать."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)

    category.add_product(product)
    assert len(category.products_list) == 1
    assert category.products_list[0] is product


# Тест 302: Позитивный тест — добавление экземпляра Smartphone в категорию работает.
def test_add_smartphone_to_category():
    """Добавление Smartphone объекта в категорию должно работать."""
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


# Тест 303: Позитивный тест — добавление экземпляра LawnGrass в категорию работает.
def test_add_lawn_grass_to_category():
    """Добавление LawnGrass объекта в категорию должно работать."""
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


# Тест 304: Негативный тест — добавление строки в категорию вызывает TypeError.
def test_add_string_to_category_raises_type_error():
    """Добавление строки в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product("не продукт")
    assert "Product" in str(exc_info.value)


# Тест 305: Негативный тест — добавление числа в категорию вызывает TypeError.
def test_add_int_to_category_raises_type_error():
    """Добавление числа в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product(123)
    assert "Product" in str(exc_info.value)


# Тест 306: Негативный тест — добавление None в категорию вызывает TypeError.
def test_add_none_to_category_raises_type_error():
    """Добавление None в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product(None)
    assert "Product" in str(exc_info.value)


# Тест 307: Негативный тест — добавление словаря в категорию вызывает TypeError.
def test_add_dict_to_category_raises_type_error():
    """Добавление словаря в категорию должно вызывать TypeError."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(name="Тестовая категория", description="Описание", products=[])
    with pytest.raises(TypeError) as exc_info:
        category.add_product({"name": "Товар"})
    assert "Product" in str(exc_info.value)


# ============================================================================
# 4. Проверка метода middle_price()
# ============================================================================


# Тест 401: Проверка, что middle_price() возвращает среднее значение цен для категории с товарами.
def test_middle_price_returns_average():
    """Метод middle_price() должен возвращать среднее значение цен всех товаров категории."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product(name="Товар 1", description="Описание", price=100.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=200.0, quantity=10)
    product3 = Product(name="Товар 3", description="Описание", price=300.0, quantity=15)

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[product1, product2, product3],
    )
    result = category.middle_price()
    assert result == 200.0  # (100 + 200 + 300) / 3 = 200.0


# Тест 402: Проверка что middle_price() возвращает 0 для пустой категории.
def test_middle_price_returns_zero_for_empty_category():
    """Метод middle_price() должен возвращать 0 для категории без товаров."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category(
        name="Пустая категория",
        description="Описание",
        products=[],
    )
    result = category.middle_price()
    assert result == 0


# Тест 403: Проверка что middle_price() возвращает float.
def test_middle_price_returns_float():
    """Метод middle_price() должен возвращать значение типа float."""
    Category.category_count = 0
    Category.product_count = 0

    product1 = Product(name="Товар 1", description="Описание", price=100.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=200.0, quantity=10)

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[product1, product2],
    )
    result = category.middle_price()
    assert isinstance(result, float)


# Тест 404: Проверка что middle_price() для одного товара возвращает его цену.
def test_middle_price_single_product():
    """Метод middle_price() для одного товара должен возвращать его цену."""
    Category.category_count = 0
    Category.product_count = 0

    product = Product(name="Товар", description="Описание", price=42.5, quantity=5)

    category = Category(
        name="Тестовая категория",
        description="Описание",
        products=[product],
    )
    result = category.middle_price()
    assert result == 42.5
