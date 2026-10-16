"""Модуль с классом Smartphone."""

from src.product import Product


class Smartphone(Product):
    """Класс Smartphone — наследник Product.

    Расширен атрибутами: производительность, модель,
    объем встроенной памяти, цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        """Инициализация смартфона.

        :param name: Название смартфона
        :param description: Описание смартфона
        :param price: Цена
        :param quantity: Количество в наличии
        :param efficiency: Производительность
        :param model: Модель
        :param memory: Объем встроенной памяти
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление смартфона."""
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
            f"Модель: {self.model}, Цвет: {self.color}"
        )
