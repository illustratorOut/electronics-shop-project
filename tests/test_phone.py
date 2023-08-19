from src.phone import Phone

item = Phone("apple", 7000, 2)
assert item.price == 7000
assert item.calculate_total_price() == 14000
assert item.apply_discount() is None and item.price == item.price * item.pay_rate

item2 = Phone("apple", 7000, 0, 2)
assert item2.number_of_sim == 2
assert repr(item2) == "Phone('apple', 7000, 0, 2)"
