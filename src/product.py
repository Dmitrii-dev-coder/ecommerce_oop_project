"""Модуль с классом Product."""


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
            raise TypeError("Можно добавлять только экземпляр Product")
        return self.price * self.quantity + other.price * other.quantity

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
