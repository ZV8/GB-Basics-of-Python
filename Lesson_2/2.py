my_list = input('Введите значения списка через запятую с пробелом: ').split(', ')
new_list = []
for i in range(0, len(my_list), 2):
    if i + 1 < len(my_list):
        new_list.append(my_list[i + 1])
    new_list.append(my_list[i])
print(f'Исходный список: {my_list}')
print(f'Модифицированный: {new_list}')
