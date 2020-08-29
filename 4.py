num = int(input('Введите число: '))
max_d = 0
while True:
    last_d = num % 10
    if max_d < last_d:
        max_d = last_d
    num = num // 10
    if num == 0:
        break
print(max_d)
