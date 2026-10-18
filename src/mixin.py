"""Модуль с классом-миксином для печати информации о создании объекта."""


class PrintInfoMixin:  # type: ignore[misc]
    """Миксин для печати информации о создании объекта.

    При создании объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        """Инициализация объекта с печатью информации.

        :param args: Позиционные аргументы для родительского класса
        :param kwargs: Именованные аргументы для родительского класса
        """
        super().__init__(*args, **kwargs)
        self._print_creation_info()

    def _print_creation_info(self) -> None:  # type: ignore[attr-defined]
        """Печатает информацию о создании объекта."""
        class_name = self.__class__.__name__
        print(
            f"{class_name}({self.name}, {self.description}, {self.price}, {self.quantity})"  # type: ignore[attr-defined]
        )
