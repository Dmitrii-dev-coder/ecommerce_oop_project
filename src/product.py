"""Модуль с классом Product."""

from src.base_product import BaseProduct
from src.mixin import PrintInfoMixin


class Product(PrintInfoMixin, BaseProduct):  # type: ignore[misc]
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
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    @property
    def price(self) -> float:  # type: ignore[no-untyped-def, override]
        """Возвращает цену продукта."""
        return self._BaseProduct__price

    @price.setter
    def price(self, value: float) -> None:  # type: ignore[no-untyped-def, override, has-type]
        """Устанавливает цену продукта.

        :param value: Новая цена
        :raises: Цена не должна быть нулевая или отрицательная
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self._BaseProduct__price:
            confirm = input("Понизить цену? (y/n): ")
            if confirm.lower() != "y":
                return
        self._BaseProduct__price = value
