"""Тесты для функции load_data."""

from src.category import Category


# ============================================================================
# 0. Проверка функции load_data для загрузки данных из JSON и создания объектов
#    Category, Product
# ============================================================================


# Тест 001: Позитивный тест — подгрузка из JSON.
def test_load_from_json():
    """Функция load_data должна создавать объекты из JSON."""
    from src.load_data import load_data

    categories = load_data("data/products.json")
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert isinstance(categories[0], Category)
