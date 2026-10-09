"""Тесты для класса Category."""

from src.product import Product
from src.category import Category


# ============================================================================
# 1. Проверка атрибутов name, description, __products, category_count, product_count в Category
# ============================================================================


# Тест 101: Позитивный тест — проверка наличия атрибута name.
def test_category_has_name(sample_category):
    """Category должен иметь атрибут name."""
    assert sample_category.name is not None


# Тест 102: Позитивный тест — проверка наличия атрибута description.
def test_category_has_description(sample_category):
    """Category должен иметь атрибут description."""
    assert sample_category.description is not None


# Тест 103: Позитивный тест — проверка наличия приватного атрибута __products.
def test_category_has_products_list(sample_category):
    """Category должен иметь приватный атрибут __products типа list."""
    assert isinstance(sample_category._Category__products, list)


# Тест 104: Позитивный тест — проверка наличия атрибута category_count.
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


# Тест 105: Позитивный тест — проверка наличия атрибута product_count.
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
# 2. Проверка метода add_product для добавления продукта в __products и product_count в Category
# ============================================================================


# Тест 201: Позитивный тест — add_product добавляет продукт в список.
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
    assert len(category._Category__products) == 1
    assert category._Category__products[0] is product


# Тест 202: Позитивный тест — add_product увеличивает product_count.
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


# Тест 203: Позитивный тест — add_product возвращает None.
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


# Тест 204: Позитивный тест — геттер products возвращает строку.
def test_products_getter_returns_string():
    """Геттер products должен возвращать строку."""
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


# Тест 205: Позитивный тест — геттер products имеет правильный формат.
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


# Тест 206: Позитивный тест — геттер products с несколькими товарами.
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
# 6. Проверка магических методов __str__ для Category
# ============================================================================


# Тест 603: Позитивный тест — __str__ для Category возвращает строку.
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


# Тест 604: Позитивный тест — __str__ для Category показывает сумму quantity.
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
