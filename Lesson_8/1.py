class MyDate:
    def __init__(self, date):
        self.date = date

    @classmethod
    def to_int(cls, item):
        try:
            ints = [int(i) for i in item.split('-')]
            if cls.valid(ints[0], ints[1], ints[2]):
                print(f'День:  {ints[0]}')
                print(f'Месяц: {ints[1]}')
                print(f'Год:   {ints[2]}')
        except ValueError:
            print('ValueError')

    @staticmethod
    def valid(d, m, y):
        valid = True
        if not 1 <= d <= 31:
            print('День должен быть указан в диапазоне от 1 до 31')
            valid = False
        if not 1 <= m <= 12:
            print('Месяц должен быть указан в диапазоне от 1 до 12')
            valid = False
        if not 1950 <= y <= 2020:
            print('Год должен быть указан в диапазоне от 1950 до 2020')
            valid = False
        return valid


print('Через класс:\n')
MyDate.to_int('32-13-2021')
print()
MyDate.to_int('3-3-2019')

print('\n--------\nЧерез объект:\n')
my_1 = MyDate('33-01-2020')
my_1.to_int(my_1.date)
print()
my_2 = MyDate('05-11-2017')
my_2.to_int(my_2.date)
