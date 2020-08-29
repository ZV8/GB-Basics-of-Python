res = int(input('Введите результат первого дня пробежки: '))
dream = int(input('Введите желаемый результат: '))
day = 1
while True:
    res *= 1.1
    day += 1
    if res >= dream:
        print(f'Результат будет достигнут на {day} день!')
        break
