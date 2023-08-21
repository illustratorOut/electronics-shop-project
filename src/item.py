from csv import DictReader
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    path_file = Path('../', 'src', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:11]

    @classmethod
    def instantiate_from_csv(cls):
        Item.all = []
        try:
            with open(cls.path_file, newline='') as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    if len(row) <= 2:
                        raise InstantiateCSVError('Файл item.csv поврежден')
                    cls(row['name'], row['price'], row['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(text):
        if text.count(".") == 1:
            return int(float(text))
        elif str(text).isdigit():
            return int(text)
        else:
            print('Страка не является числом')

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise ValueError(f'Сложение не возможно не является экземпляром класса {self.__class__.__name__}')


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.value = args if args else 'Файл item.csv поврежден'

    def __str__(self):
        return f"{self.value}"
