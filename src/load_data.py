"""Модуль для загрузки данных из JSON-файла."""

import json

from src.product import Product
from src.category import Category


def load_data(filepath: str) -> list:
    """Загрузка данных из JSON-файла.

    :param filepath: Путь к JSON-файлу
    :return: Список категорий с продуктами
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = [
            Product(
                name=p["name"],
                description=p["description"],
                price=p["price"],
                quantity=p["quantity"],
            )
            for p in category_data["products"]
        ]
        categories.append(
            Category(
                name=category_data["name"],
                description=category_data["description"],
                products=products,
            )
        )
    return categories


# Сброс счётчиков при импорте модуля
Category.category_count = 0
Category.product_count = 0
