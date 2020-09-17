class Cell:
    def __init__(self, cells):
        self.__cells = cells

    def __add__(self, other):
        return f'Сложение: {self.__cells + other.__cells}'

    def __sub__(self, other):
        return f'Вычитание: {self.__cells - other.__cells}' \
            if self.__cells - other.__cells > 0 else 'Вычитание: недопустимая операция'

    def __mul__(self, other):
        return f'Умножение: {self.__cells * other.__cells}'

    def __floordiv__(self, other):
        return f'Деление: {self.__cells // other.__cells}'

    def make_order(self, num):
        output = ''
        temp = self.__cells // num
        for temp in range(temp):
            output += f"{'*' * num}\n"
        if self.__cells % num:
            output += f"{'*' * (self.__cells - self.__cells // num * num)}\n"
        return output


cell_1 = Cell(10)
cell_2 = Cell(22)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print()
print(cell_2.make_order(6))
