"""Модуль с классом LawnGrass."""

from src.product import Product


class LawnGrass(Product):
    """Класс LawnGrass — наследник Product.

    Расширен атрибутами: страна-производитель,
    срок прорастания, цвет.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Инициализация газонной травы.

        :param name: Название травы
        :param description: Описание травы
        :param price: Цена
        :param quantity: Количество в наличии
        :param country: Страна-производитель
        :param germination_period: Срок прорастания
        :param color: Цвет
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Возвращает строковое представление газонной травы."""
        return (
            f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
            f"Страна: {self.country}, Цвет: {self.color}"
        )
