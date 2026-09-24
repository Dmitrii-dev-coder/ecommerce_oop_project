"""Модуль с классами Product и Category."""


class Product:
    """Класс Product."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация продукта.

        :param name: Название продукта
        :param description: Описание продукта
        :param price: Цена
        :param quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
