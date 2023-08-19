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

    item4 = Item("apple", 435, 5)
    assert item4.name == "apple"

    item5 = Item("apple", 435, 5)
    pear = item5.name = "pear"
    assert pear == "pear"
    orange = item5.name = "orange_lime_d"
    assert item5.name == "orange_lime"

    item6 = Item("apple", 100, 10)
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('Dima') is None

    item7 = Item("Смартфон", 10000, 20)
    assert repr(item7) == "Item('Смартфон', 10000, 20)"
    assert str(item7) == 'Смартфон'




