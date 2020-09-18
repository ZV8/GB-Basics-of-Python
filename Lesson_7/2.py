from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def needs(self):
        pass


class Coat(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def needs(self):
        return f'Расход ткани для {self.name}: {round(self.param / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)

    @property
    def needs(self):
        return f'Расход ткани для {self.name}: {round(2 * self.param + 0.3, 2)}'


my_1 = Coat('Пальто_1', 6.5)
my_2 = Coat('Пальто_2', 7)
my_3 = Suit('Костюм_1', 5)
print(my_1.needs)
print(my_2.needs)
print(my_3.needs)
