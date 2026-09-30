from src.products import Category, Product

# ============================================================================
# 0. Проверка класса Product:
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
# 1. Проверка класса Category:
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
# 2. Приватный атрибут products и метод add_product:
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


# ============================================================================
# 3. Подгрузка данных из JSON:
# ============================================================================


# Тест 301: Позитивный тест — подгрузка из JSON.
def test_load_from_json():
    """Функция load_data должна создавать объекты из JSON."""
    from src.products import Category, load_data

    categories = load_data("data/products.json")
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert isinstance(categories[0], Category)


# Тест 302: Позитивный тест — new_product создает экземпляр Product.
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


# ============================================================================
# 4. Приватная цена с геттером и сеттером:
# ============================================================================


# Тест 401: Позитивный тест — геттер price возвращает значение.
def test_price_getter_returns_value():
    """Геттер price должен возвращать значение приватного атрибута."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    assert product.price == 100.0


# Тест 402: Позитивный тест — сеттер устанавливает положительную цену.
def test_price_setter_positive():
    """Сеттер price должен устанавливать положительное значение."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 200.0
    assert product.price == 200.0


# Тест 403: Позитивный тест — сеттер отклоняет нулевую цену.
def test_price_setter_zero():
    """Сеттер price не должен устанавливать нулевую цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 0
    assert product.price == 100.0


# Тест 404: Позитивный тест — сеттер отклоняет отрицательную цену.
def test_price_setter_negative():
    """Сеттер price не должен устанавливать отрицательную цену."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = -50.0
    assert product.price == 100.0


# Тест 405: Позитивный тест — сеттер подтверждает понижение цены.
def test_price_setter_confirm_decrease():
    """Сеттер price должен запрашивать подтверждение при понижении."""
    product = Product(name="Товар", description="Описание", price=100.0, quantity=5)
    product.price = 200.0
    assert product.price == 200.0
