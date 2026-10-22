"""Модуль с классом-миксином для печати информации о создании объекта."""


class PrintInfoMixin:
    """Миксин для печати информации о созданном объекте.

    При создании объекта печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект.
    """

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        """Инициализация объекта с печатью информации."""
        super().__init__(*args, **kwargs)
        print(repr(self))

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return (
            f"{self.__class__.__name__}("
            f"'{self.name}', "  # type: ignore[attr-defined]
            f"'{self.description}', "  # type: ignore[attr-defined]
            f"{self.price}, "  # type: ignore[attr-defined]
            f"{self.quantity})"  # type: ignore[attr-defined]
        )
