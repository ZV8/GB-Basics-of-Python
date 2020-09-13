import time
from colorama import Fore


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed=0):
        self.speed = new_speed if new_speed else self.speed
        print(f'{self.color} {self.name} движется', end='')
        self.show_speed()
        print('---')
        time.sleep(2)

    def stop(self):
        print(f'{self.color} {self.name} остановилась')
        print('---')
        time.sleep(2)

    def turn(self, direction):
        print(f'{self.color} {self.name} повернула {direction}')
        print('---')
        time.sleep(2)

    def show_speed(self):
        print(f' со скоростью {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print(f'{Fore.RED}Превышение скорости для {self.name} на {self.speed - 60} км/ч!{Fore.RESET}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print(f'Превышение скорости для WorkCar {self.name}!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.name = 'полицейский ' + self.name


car_1 = TownCar(55, 'серый', 'Такси')
print('Новый объект:', car_1.name, car_1.color, car_1.speed, car_1.is_police)
car_1.go()
car_1.stop()
car_1.go(200)

car_2 = TownCar(70, 'белый', 'Автобус')
print('Новый объект:', car_2.name, car_2.color, car_2.speed, car_2.is_police)
car_2.go()
car_2.go(40)
car_2.stop()
car_2.go()
car_2.turn('налево')
car_2.turn('прямо')
car_2.go(50)
car_2.go(70)

car_3 = PoliceCar(90, 'неопознанный', 'Фургон')
print('Новый объект:', car_3.name, car_3.color, car_3.speed, car_3.is_police)
car_3.turn('прямо')
car_3.go(50)
