"""Модуль с классом Category."""

from src.product import Product


class Category:
    """Класс Category."""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список продуктов
        """
        self.name = name
        self.description = description
        self.__products = list(products)
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Возвращает строковое представление категории.

        Формат: "Название категории, количество продуктов: X шт."
        Количество продуктов — сумма quantity всех продуктов на складе.
        """
        total_quantity = sum(product.quantity for product in self.products_list)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products_list(self) -> list[Product]:
        """Возвращает список продуктов в категории.

        :return: Список объектов Product
        """
        return self.__products

    def add_product(self, product: Product) -> None:
        """Добавить продукт в категорию.

        Использует try/except/else/finally для обработки ошибок.

        :param product: Экземпляр класса Product или его наследника
        :raises TypeError: Если передан объект не типа Product
        """
        try:
            if not isinstance(product, Product):
                raise TypeError(
                    "Можно добавлять только объекты типа Product или его наследников"
                )
        except TypeError as e:
            print(e)
            raise
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self) -> float:
        """Подсчитать средний ценник всех товаров в категории.

        Складывает цены (self.price) всех товаров и делит на количество.
        Если товаров нет — возвращает 0.

        :return: Средний ценник или 0 если товаров нет
        """
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    @property
    def products(self) -> str:
        """Возвращает строку со всеми продуктами.

        Формат: "Название продукта, X руб. Остаток: X шт.\n"
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
