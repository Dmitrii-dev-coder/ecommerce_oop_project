"""Тесты для класса Product."""

import pytest
import unittest.mock

from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


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
# 1. Проверка класс-метода new_product для создания Product из словаря
# ============================================================================


# Тест 101: Позитивный тест — new_product создает экземпляр Product.
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


# Тест 102: Позитивный тест — new_product корректно передаёт все данные.
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
# 2. Проверка __price из Product, геттера price, сеттера price на положительное
#    значение и подтверждением понижения
# ============================================================================


# Тест 201: Позитивный тест — геттер price возвращает значение.
def test_price_getter_returns_value():
    """Геттер price должен возвращать значение приватного атрибута."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert product.price == 100.0


# Тест 202: Позитивный тест — сеттер устанавливает положительную цену.
def test_price_setter_positive():
    """Сеттер price должен устанавливать положительное значение."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 200.0
    assert product.price == 200.0


# Тест 203: Позитивный тест — сеттер отклоняет нулевую цену.
def test_price_setter_zero():
    """Сеттер price не должен устанавливать нулевую цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 0
    assert product.price == 100.0


# Тест 204: Позитивный тест — сеттер отклоняет отрицательную цену.
def test_price_setter_negative():
    """Сеттер price не должен устанавливать отрицательную цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = -50.0
    assert product.price == 100.0


# Тест 205: Позитивный тест — подтверждение понижения цены с "y".
def test_price_setter_confirm_decrease_with_yes():
    """Сеттер price должен понизить цену при подтверждении 'y'."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="y"):
        product.price = 50.0
    assert product.price == 50.0


# Тест 206: Позитивный тест — отказ от понижения цены с "n".
def test_price_setter_confirm_decrease_with_no():
    """Сеттер price не должен понижать цену при отказе 'n'."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="n"):
        product.price = 50.0
    assert product.price == 100.0


# Тест 207: Позитивный тест — отказ от понижения цены с "N" (заглавная).
def test_price_setter_confirm_decrease_with_N():
    """Сеттер price не должен понижать цену при отказе 'N' (заглавная)."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="N"):
        product.price = 50.0
    assert product.price == 100.0


# Тест 208: Позитивный тест — отказ от понижения цены с любым другим ответом.
def test_price_setter_confirm_decrease_with_other():
    """Сеттер price не должен понижать цену при любом ответе кроме 'y'."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    with unittest.mock.patch("builtins.input", return_value="yes"):
        product.price = 50.0
    assert product.price == 100.0


# Тест 209: Позитивный тест — установка цены равной текущей.
def test_price_setter_equal_to_current():
    """Сеттер price должен устанавливать цену равную текущей."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 100.0
    assert product.price == 100.0


# ============================================================================
# 3. Проверка магических методов __str__ для Product
# ============================================================================


# Тест 301: Позитивный тест — __str__ для Product возвращает строку.
def test_product_str_returns_string():
    """Метод __str__ для Product должен возвращать строку."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    result = str(product)
    assert isinstance(result, str)
    assert "Товар" in result
    assert "100.0" in result
    assert "5" in result


# Тест 302: Позитивный тест — __str__ для Product имеет правильный формат.
def test_product_str_format():
    """Метод __str__ для Product должен возвращать строку в формате: Название, X руб. Остаток: X шт."""
    product = Product(name="Смартфон", description="Смартфон с хорошей камерой", price=50000.0, quantity=25)
    result = str(product)
    assert "Смартфон, 50000.0 руб. Остаток: 25 шт." in result


# ============================================================================
# 4. Проверка магического метода __add__ для Product
# ============================================================================


# Тест 401: Позитивный тест — __add__ возвращает сумму цен с учётом количества.
def test_product_add_returns_sum():
    """Метод __add__ должен возвращать сумму (цена * количество) двух продуктов."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert result == 110.0


# Тест 402: Позитивный тест — __add__ возвращает float.
def test_product_add_returns_float():
    """Метод __add__ должен возвращать значение типа float."""
    product1 = Product(name="Товар 1", description="Описание", price=10.0, quantity=5)
    product2 = Product(name="Товар 2", description="Описание", price=20.0, quantity=3)
    result = product1 + product2
    assert isinstance(result, float)


# Тест 403: Позитивный тест — __add__ с продуктами одинаковой цены.
def test_product_add_same_price():
    """Метод __add__ должен корректно складывать продукты с одинаковой ценой."""
    product1 = Product(name="Товар 1", description="Описание", price=50.0, quantity=10)
    product2 = Product(name="Товар 2", description="Описание", price=50.0, quantity=10)
    result = product1 + product2
    assert result == 1000.0


# Тест 404: Негативный тест — сложение Product со строкой вызывает TypeError.
def test_product_add_invalid_type():
    """Метод __add__ должен вызывать TypeError для не Product объектов."""
    product = Product(name="Товар", description="Описание", price=10.0, quantity=5)
    with pytest.raises(TypeError) as exc_info:
        product + "не продукт"
    assert "одного класса" in str(exc_info.value)


# ============================================================================
# 5. Проверка обработки нулевого и отрицательного количества при создании экземпляров Product, Smartphone и LawnGrass
# ============================================================================


# Тест 501: Негативный тест — создание Product с нулевым количеством вызывает ValueError.
def test_product_zero_quantity_raises_value_error():
    """Создание экземпляра Product с quantity=0 должно выбрасывать ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product(name="Товар", description="Описание", price=10.0, quantity=0)
    assert "нулевым количеством" in str(exc_info.value)


# Тест 502: Позитивный тест — создание Product с quantity>0 работает корректно.
def test_product_positive_quantity_works():
    """Создание экземпляра Product с quantity>0 должно работать."""
    product = Product(name="Товар", description="Описание", price=10.0, quantity=5)
    assert product.quantity == 5


# Тест 503: Негативный тест — создание Smartphone с quantity=0 вызывает ValueError.
def test_smartphone_zero_quantity_raises_value_error():
    """Создание экземпляра Smartphone с quantity=0 должно выбрасывать ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Smartphone(
            name="iPhone 15",
            description="Флагманский смартфон Apple",
            price=99990.0,
            quantity=0,
            efficiency="high",
            model="iPhone 15 Pro",
            memory="256GB",
            color="Черный",
        )
    assert "нулевым количеством" in str(exc_info.value)


# Тест 504: Позитивный тест — создание Smartphone с quantity>0 работает корректно.
def test_smartphone_positive_quantity_works():
    """Создание экземпляра Smartphone с quantity>0 должно работать."""
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


# Тест 505: Негативный тест — создание LawnGrass с quantity=0 вызывает ValueError.
def test_lawn_grass_zero_quantity_raises_value_error():
    """Создание экземпляра LawnGrass с quantity=0 должно выбрасывать ValueError."""
    with pytest.raises(ValueError) as exc_info:
        LawnGrass(
            name="Газон 1",
            description="Смесь газонных трав",
            price=500.0,
            quantity=0,
            country="Россия",
            germination_period="14 дней",
            color="Зеленый",
        )
    assert "нулевым количеством" in str(exc_info.value)


# Тест 506: Позитивный тест — создание LawnGrass с quantity>0 работает корректно.
def test_lawn_grass_positive_quantity_works():
    """Создание экземпляра LawnGrass с quantity>0 должно работать."""
    lawn_grass = LawnGrass(
        name="Газон 1",
        description="Смесь газонных трав",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="14 дней",
        color="Зеленый",
    )
    assert lawn_grass.quantity == 20


# ============================================================================
# 6. Проверка ограничений сложения через type()
# ============================================================================


# Тест 601: Позитивный тест — сложение двух экземпляров Smartphone работает.
def test_add_two_smartphone():
    """Сложение двух экземпляров Smartphone объектов должно работать."""
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
    assert result == 1449850.0


# Тест 602: Позитивный тест — сложение двух LawnGrass работает.
def test_add_two_lawn_grass():
    """Сложение двух экземпляров LawnGrass объектов должно работать."""
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
    assert result == 19000.0


# Тест 603: Негативный тест — сложение Smartphone и LawnGrass вызывает TypeError.
def test_add_smartphone_and_lawn_grass_raises_type_error():
    """Сложение экземпляра Smartphone и экземпляра LawnGrass должно вызывать TypeError."""
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


# Тест 604: Негативный тест — сложение Smartphone и Product вызывает TypeError.
def test_add_smartphone_and_product_raises_type_error():
    """Сложение экземпляра Smartphone и экземпляра Product должно вызывать TypeError."""
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


# Тест 605: Негативный тест — сложение LawnGrass и Product вызывает TypeError.
def test_add_lawn_grass_and_product_raises_type_error():
    """Сложение экземпляра LawnGrass и экземпляра Product должно вызывать TypeError."""
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
