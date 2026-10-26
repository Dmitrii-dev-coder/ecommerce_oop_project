"""Модуль с классом Product."""

from src.base_product import BaseProduct
from src.mixin import PrintInfoMixin


class Product(BaseProduct, PrintInfoMixin):
    """Класс Product для представления товара.

    Наследуется от BaseProduct (абстрактный базовый класс с общей функциональностью)
    и PrintInfoMixin (для печати информации).
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена
        :param quantity: Количество в наличии
        :raises ValueError: Если количество равно нулю или отрицательное
        """
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        # Сначала инициализируем атрибуты, которые нужны mixin
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price
        # Затем вызываем super для печати информации (без аргументов)
        super().__init__()
        # Устанавливаем цену через сеттер (с проверкой)
        self.price = price

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Возвращает сумму цен двух продуктов с учётом количества.

        Складывать можно только объекты одного класса.

        :param other: Другой экземпляр продукта
        :return: Сумма (цена * количество) текущего и другого продукта
        :raises TypeError: Если объекты разных классов
        """
        if type(self) is not type(other):  # noqa: E721
            raise TypeError(
                "Можно складывать только объекты одного класса (Product или его наследников)"
            )
        return self.price * self.quantity + other.price * other.quantity

    @property
    def price(self) -> float:  # type: ignore[attr-defined]
        """Возвращает цену продукта."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:  # type: ignore[attr-defined]
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
        :return: Экземпляр Product
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )
