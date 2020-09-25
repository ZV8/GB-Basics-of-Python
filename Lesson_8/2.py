class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if b == 0:
        raise ZeroDivError("Деление на ноль невозможно!")
except ValueError:
    print("Вы ввели не число")
except ZeroDivError as err:
    print(err)
else:
    print(f"Результат деления первого числа на второе: {a / b}")
