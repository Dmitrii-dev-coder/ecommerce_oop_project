"""Модуль с классом-миксином для печати информации о создании объекта."""


class PrintInfoMixin:
    """Миксин для печати информации о создании объекта.

    При создании объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self) -> None:
        """Инициализация объекта с печатью информации."""
        super().__init__()
        self._print_creation_info()

    def _print_creation_info(self) -> None:
        """Подготавливает данные для вывода информации о создании объекта."""
        class_name = self.__class__.__name__
        self._print_info(class_name)

    def _print_info(self, class_name: str) -> None:  # type: ignore[attr-defined]
        """Печатает информацию с указанием класса.

        :param class_name: Имя класса
        """
        print(
            f"{class_name}({self.name}, {self.description}, "  # type: ignore[attr-defined]
            f"{self.price}, {self.quantity})"  # type: ignore[attr-defined]
        )
