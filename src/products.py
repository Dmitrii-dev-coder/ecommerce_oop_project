"""Модуль с классами Product и Category."""

import json


class Product:
    """Класс Product."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ):
        """Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Устанавливает цену продукта.

        :param value: Новая цена
        :raises: Цена не должна быть нулевая или отрицательная
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            confirm = input("Понизить цену? (y/n): ")
            if confirm.lower() != "y":
                return
        self.__price = value

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        """Создать продукт из словаря.

        :param product_data: Словарь с данными продукта
        :return: Экземпляр класса Product
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """Возвращает сумму цен двух продуктов с учётом количества.

        :param other: Другой экземпляр Product
        :return: Сумма (цена * количество) текущего и другого продукта
        """
        if not isinstance(other, Product):
            raise TypeError("Can only add Product instances")
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """Класс Category."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категории."""
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: "Product") -> None:
        """Добавить продукт в категорию.

        :param product: Экземпляр класса Product
        """
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        return f"Категория: {self.name}, Описание: {self.description}, Товаров: {len(self._Category__products)}"

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами.

        Формат: "Название продукта, X руб. Остаток: X шт.\n"
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result


def load_data(filepath: str) -> list:
    """Загрузка данных из JSON-файла."""
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"],
            )
            for p in category_data["products"]
        ]
        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )
    return categories


# Сброс счётчиков при импорте модуля
Category.category_count = 0
Category.product_count = 0
