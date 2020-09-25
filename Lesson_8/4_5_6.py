from abc import ABC, abstractmethod


class Int123Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, equipments=None):
        if equipments is None:
            equipments = {
                'Принтер': [],
                'Сканер': [],
                'Ксерокс': []
            }
        self.equipments = equipments
        self.amount = self.count()

    def count(self):
        return {a: len(b) for a, b in self.equipments.items()}

    def all_count(self):
        print(f'\nВсего товаров на складе:')
        for ind, el in self.count().items():
            print(f'{ind}: {el} шт.')

    def eq_list(self, eq_type):
        print(f'\n---')
        print(f'"{eq_type.upper()}" В НАЛИЧИИ НА СКЛАДЕ: {self.count()[eq_type]} шт.')
        print(f'Серийный номер      № ячейки')
        for n, i in enumerate(self.equipments[eq_type]):
            print(f'SN: {i["serial_number"].ljust(12, " ")}->    {n}')
        print(f'---')

    def add(self, item):
        self.equipments[item.name]\
            .append({'serial_number': item.serial_number, 'brand': item.brand})
        self.amount = self.count()
        print(f'\nОборудование "{item.name}" с серийным номером "{item.serial_number}" бренда "{item.brand}" добавлено на склад!')

    def move_to_division(self, eq_type, num_menu, division):
        print(f'---')
        sn = self.equipments[eq_type][num_menu].get("serial_number")
        del self.equipments[eq_type][num_menu]
        print(f'{eq_type} с серийным номером {sn} перемещен в {division}')
        self.all_count()


class OfficeEquipment(ABC):
    def __init__(self, serial_number, brand):
        self.brand = brand
        self.serial_number = serial_number

    @abstractmethod
    def name(self):
        pass


class Printer(OfficeEquipment):
    def work(self):
        print(f'Принтер {self.serial_number} печатает')

    @property
    def name(self):
        return 'Принтер'


class Scanner(OfficeEquipment):
    def work(self):
        print(f'Сканер {self.serial_number} сканирует')

    @property
    def name(self):
        return 'Сканер'


class Xerox(OfficeEquipment):
    def work(self):
        print(f'Ксерокс {self.serial_number} ксерокопирует')

    @property
    def name(self):
        return 'Ксерокс'


class Menu:
    whs = None

    @classmethod
    def main(cls, whs):
        cls.whs = whs
        print(f'\n=======================================')
        print(f'Пункты меню:')
        print(f'1 - Помотреть список оборудования на складе')
        print(f'2 - Помотреть детально по типу оборудования')
        print(f'3 - Добавить оборудование на склад')
        print(f'4 - Переместить оборудование со склада в подразделение компании')
        print(f'---------------------------------------')
        cls.input_menu()

    @classmethod
    def input_menu(cls):
        print()
        i = input('Введите пункт меню ("m" - меню; "q" - выход): ')
        if i == 'q':
            print('Программа завершена. Всего доброго!')
        elif i == 'm':
            cls.main(cls.whs)
        else:
            if i.isdigit():
                if 0 < int(i) < 5:
                    # return int(i)
                    if int(i) == 1:
                        return cls.menu_1()
                    if int(i) == 2:
                        return cls.menu_2()
                    if int(i) == 3:
                        return cls.menu_3()
                    if int(i) == 4:
                        return cls.menu_4()
                else:
                    print('Значение должно быть в диапазоне от 1 до 4!')
                    return cls.input_menu()
            else:
                print('Некорретный ввод значения!')
                return cls.input_menu()

    @classmethod
    def menu_1(cls):
        cls.whs.all_count()
        return cls.input_menu()

    @classmethod
    def menu_2(cls):
        try:
            inp = int(input('\nКакое оборудование смотрим?\n1 - Принтеры\n2 - Сканеры\n3 - Копиры\nВведите число: '))
            if not 1 <= inp <= 3:
                raise Int123Error("\nТолько цифры от 1 до 3!")
        except (ValueError, Int123Error):
            print('\nТолько цифры от 1 до 3!')
            return cls.menu_2()
        else:
            cls.whs.eq_list({1: 'Принтер', 2: 'Сканер', 3: 'Ксерокс'}.get(inp))
            return cls.input_menu()

    @classmethod
    def menu_3(cls):
        item = None
        try:
            inp = int(input('\nКакое оборудование добавляем?\n1 - Принтер\n2 - Сканер\n3 - Копир\nВведите число: '))
            if not 1 <= inp <= 3:
                raise Int123Error("\nТолько цифры от 1 до 3!")
        except (ValueError, Int123Error):
            print('\nТолько цифры от 1 до 3!')
            return cls.menu_3()
        else:
            if inp == 1:
                item = Printer(input('Введите серийный номер: '), input('Введите бренд: '))
            if inp == 2:
                item = Scanner(input('Введите серийный номер: '), input('Введите бренд: '))
            if inp == 3:
                item = Xerox(input('Введите серийный номер: '), input('Введите бренд: '))
            cls.whs.add(item)
            cls.whs.eq_list({1: 'Принтер', 2: 'Сканер', 3: 'Ксерокс'}.get(inp))
            return cls.input_menu()

    @classmethod
    def menu_4(cls, inp=None):
        try:
            if not inp:
                inp = int(input('\nКакое оборудование перемещаем?\n1 - Принтер\n2 - Сканер\n3 - Копир\nВведите число: '))
                if not 1 <= inp <= 3:
                    raise Int123Error("\nТолько цифры от 1 до 3!")
        except (ValueError, Int123Error):
            print('\nТолько цифры от 1 до 3!')
            return cls.menu_4()
        else:
            tmp = {1: 'Принтер', 2: 'Сканер', 3: 'Ксерокс'}.get(inp)
            cls.whs.eq_list(tmp)
            if not len(cls.whs.equipments.get(tmp)):
                print(f'\nНевозможно переместить! Устройства типа "{tmp}" на складе не обнаружены!')
                return cls.input_menu()
            else:
                try:
                    num = int(input('Введите номер ячейки хранения устройства: '))
                    if num not in range(0, len(cls.whs.equipments.get(tmp))):
                        raise Int123Error("\nТолько цифры соответствующие номерам ячеек!")
                except (ValueError, Int123Error):
                    print('\nТолько цифры соответствующие номерам ячеек!')
                    return cls.menu_4(inp)
                else:
                    cls.whs.move_to_division(tmp, num, input('Куда перемещаем? (произвольное название): '))
                    return cls.input_menu()


office_equipments = {
    'Принтер': [{'serial_number': '1111111', 'brand': 'HP'}, {'serial_number': '222222', 'brand': 'HP'}],
    'Сканер': [{'serial_number': '2222222', 'brand': 'Epson'}],
    'Ксерокс': [{'serial_number': '3333333', 'brand': 'Xerox'}]
}

wh = Warehouse(office_equipments)
Menu.main(wh)
