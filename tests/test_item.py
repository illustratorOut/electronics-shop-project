"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    item = Item("apple", 7000, 2)
    assert item.price == 7000
    assert item.calculate_total_price() == 14000
    assert item.apply_discount() is None and item.price == item.price * item.pay_rate

    item2 = Item("apple", 7000, 0)
    assert item2.calculate_total_price() == 0

    item3 = Item("apple", 0, 4)
    assert item3.calculate_total_price() == 0
