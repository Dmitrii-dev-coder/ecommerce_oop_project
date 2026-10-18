"""Модуль с классом Product."""

from src.base_product import BaseProduct
from src.mixin import PrintInfoMixin


class Product(PrintInfoMixin, BaseProduct):
    """Класс Product для представления товара.

    Наследуется от PrintInfoMixin (для печати информации) и BaseProduct
    (абстрактный базовый класс с общей функциональностью).
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
        """
        # Сначала инициализируем атрибуты, которые нужны mixin
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price
        # Затем вызываем super для печати информации (без аргументов)
        super().__init__()
        # Устанавливаем цену через сеттер (с проверкой)
        self.price = price

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
