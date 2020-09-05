def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на 0 невозможно!'


def input_float(mess):
    try:
        num = float(input(mess))
        return num
    except ValueError:
        print('Значение должно быть числом!')
        return input_float(mess)


my_a = input_float('Введите число a: ')
my_b = input_float('Введите число b: ')
print(division(my_a, my_b))
