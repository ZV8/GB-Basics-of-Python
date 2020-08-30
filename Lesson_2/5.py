num = int(input('Введите новый элемент рейтинга (число): '))
my_list = [7, 5, 3, 3, 2]
index = 0
for ind, el in enumerate(my_list):
    if num <= el:
        index = ind + 1
my_list.insert(index, num)
print(my_list)
