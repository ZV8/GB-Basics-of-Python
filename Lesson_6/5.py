class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки для ручки {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки для карандаша {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки для маркера {self.title}')


item_1 = Pen('Erich Krause')
item_1.draw()

item_2 = Pencil('Каляка-Маляка')
item_2.draw()

item_3 = Handle('Lyra')
item_3.draw()
