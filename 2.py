sec = int(input('Введите время в секундах: '))
h = sec // 3600
m = sec % 3600 // 60
s = sec % 3600 % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
