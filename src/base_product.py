"""Модуль с абстрактным базовым классом BaseProduct."""

from abc import ABC, abstractmethod


class BaseProduct(ABC):  # type: ignore[attr-defined]
    """Абстрактный базовый класс для всех продуктов.

    Определяет контракт для всех продуктов — абстрактный метод price (геттер/сеттер).
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
