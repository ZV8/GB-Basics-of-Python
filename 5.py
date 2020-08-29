deb = int(input('Введите сумму выручки: '))
cred = int(input('Введите сумму издержек: '))
result = deb - cred
profit = False
if result > 0:
    print(f'Прибыль: {result}')
    profit = True
elif result < 0:
    print(f'Убыток: {result}')
else:
    print(f'Сработали в ноль')
if profit:
    rent = result / deb
    print(f'Рентабельность выручки: {result / deb * 100}%')
    workers = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {result / workers}')
