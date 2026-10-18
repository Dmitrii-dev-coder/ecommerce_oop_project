"""Модуль с абстрактным базовым классом BaseProduct."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):  # type: ignore[attr-defined]
    """Абстрактный базовый класс для всех продуктов.

    Определяет контракт для всех продуктов:
    - name: str — название
    - description: str — описание
    - price: float — цена (через абстрактный property)
    - quantity: int — количество
    """

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный метод для получения цены.

        :return: Цена продукта
        """
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        """Абстрактный метод для установки цены.

        :param value: Новая цена
        """
        pass

    @classmethod
    def new_product(cls, product_data: dict) -> "BaseProduct":  # type: ignore[no-untyped-def, call-arg]
        """Создать продукт из словаря.

        :param product_data: Словарь с данными продукта
        :return: Экземпляр класса
        """
        return cls(  # type: ignore[call-arg]
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."  # type: ignore[attr-defined]

    def __add__(self, other: "BaseProduct") -> float:
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
        return self.price * self.quantity + other.price * other.quantity  # type: ignore[attr-defined]
