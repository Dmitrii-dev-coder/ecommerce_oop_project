"""Тесты для класса Product."""

import unittest.mock

from src.product import Product


# ============================================================================
# 0. Проверка наличия атрибутов name, description, price, quantity в классе Product
# ============================================================================


# Тест 001: Позитивный тест — проверка наличия атрибута name.
def test_product_has_name(sample_product):
    """Product должен иметь атрибут name."""
    assert sample_product.name is not None


# Тест 002: Позитивный тест — проверка наличия атрибута description.
def test_product_has_description(sample_product):
    """Product должен иметь атрибут description."""
    assert sample_product.description is not None


# Тест 003: Позитивный тест — проверка наличия атрибута price.
def test_product_has_price(sample_product):
    """Product должен иметь атрибут price."""
    assert sample_product.price is not None


# Тест 004: Позитивный тест — проверка наличия атрибута quantity.
def test_product_has_quantity(sample_product):
    """Product должен иметь атрибут quantity."""
    assert sample_product.quantity is not None


# ============================================================================
# 3. Проверка класс-метода new_product для создания Product из словаря
# ============================================================================


# Тест 301: Позитивный тест — new_product создает экземпляр Product.
def test_new_product_creates_instance():
    """Метод new_product должен создавать объект Product."""
    product_data = {
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 100.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert isinstance(product, Product)
    assert product.name == "Тестовый товар"
    assert product.price == 100.0
    assert product.quantity == 10


# Тест 302: Позитивный тест — new_product корректно передаёт все данные.
def test_new_product_correct_data():
    """Метод new_product должен корректно передавать все данные из словаря."""
    product_data = {
        "name": "Новый телефон",
        "description": "Смартфон с хорошей камерой",
        "price": 50000.0,
        "quantity": 25,
    }
    product = Product.new_product(product_data)
    assert product.name == "Новый телефон"
    assert product.description == "Смартфон с хорошей камерой"
    assert product.price == 50000.0
    assert product.quantity == 25


# ============================================================================
# 5. Проверка __price из Product, геттера price, сеттера price на положительное
#    значение и подтверждением понижения
# ============================================================================


# Тест 501: Позитивный тест — геттер price возвращает значение.
def test_price_getter_returns_value():
    """Геттер price должен возвращать значение приватного атрибута."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert product.price == 100.0


# Тест 502: Позитивный тест — сеттер устанавливает положительную цену.
def test_price_setter_positive():
    """Сеттер price должен устанавливать положительное значение."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 200.0
    assert product.price == 200.0


# Тест 503: Позитивный тест — сеттер отклоняет нулевую цену.
def test_price_setter_zero():
    """Сеттер price не должен устанавливать нулевую цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 0
    assert product.price == 100.0


# Тест 504: Позитивный тест — сеттер отклоняет отрицательную цену.
def test_price_setter_negative():
    """Сеттер price не должен устанавливать отрицательную цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = -50.0
    assert product.price == 100.0


# Тест 505: Позитивный тест — подтверждение понижения цены с "y".
def test_price_setter_confirm_decrease_with_yes():
    """Сеттер price должен понизить цену при подтверждении 'y'."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="y"):
        product.price = 50.0
    assert product.price == 50.0


# Тест 506: Позитивный тест — отказ от понижения цены с "n".
def test_price_setter_confirm_decrease_with_no():
    """Сеттер price не должен понижать цену при отказе 'n'."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="n"):
        product.price = 50.0
    assert product.price == 100.0


# ============================================================================
# 6. Проверка магических методов __str__ для Product
# ============================================================================


# Тест 601: Позитивный тест — __str__ для Product возвращает строку.
def test_product_str_returns_string():
    """Метод __str__ для Product должен возвращать строку."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    result = str(product)
    assert isinstance(result, str)
    assert "Товар" in result
    assert "100.0" in result
    assert "5" in result


# Тест 602: Позитивный тест — __str__ для Product имеет правильный формат.
def test_product_str_format():
    """Метод __str__ для Product должен возвращать строку в формате: Название, X руб. Остаток: X шт."""
    product = Product(name="Смартфон", description="Смартфон с хорошей камерой", price=50000.0, quantity=25)
    result = str(product)
    assert "Смартфон, 50000.0 руб. Остаток: 25 шт." in result


# ============================================================================
# 7. Проверка магического метода __add__ для Product
# ============================================================================


# Тест 701: Позитивный тест — __add__ возвращает сумму цен с учётом количества.
def test_product_add_returns_sum():
    """Метод __add__ должен возвращать сумму (цена * количество) двух продуктов."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert result == 10.0 * 5 + 20.0 * 3
    assert result == 110.0


# Тест 702: Позитивный тест — __add__ возвращает float.
def test_product_add_returns_float():
    """Метод __add__ должен возвращать значение типа float."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert isinstance(result, float)


# Тест 703: Позитивный тест — __add__ с продуктами одинаковой цены.
def test_product_add_same_price():
    """Метод __add__ должен корректно складывать продукты с одинаковой ценой."""
    product1 = Product(name="Товар 1", description="Описание", price=50.0, quantity=10)
    product2 = Product(name="Товар 2", description="Описание", price=50.0, quantity=10)
    result = product1 + product2
    assert result == 50.0 * 10 + 50.0 * 10
    assert result == 1000.0


# Тест 704: Позитивный тест — __add__ с нулевым количеством.
def test_product_add_zero_quantity():
    """Метод __add__ должен корректно обрабатывать продукты с нулевым количеством."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=0)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=5)
    result = product1 + product2
    assert result == 10.0 * 0 + 20.0 * 5
    assert result == 100.0


# Тест 705: Негативный тест — __add__ с не Product объектом вызывает TypeError.
def test_product_add_invalid_type():
    """Метод __add__ должен вызывать TypeError для не Product объектов."""
    product = Product(name="Товар", description="Описание", price=10.0, quantity=5)
    try:
        product + "не продукт"
        assert False, "TypeError не был вызван"
    except TypeError as e:
        assert "Can only add Product instances" in str(e)
