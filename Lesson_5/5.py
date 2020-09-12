import random

with open("05.txt", "w+", encoding="utf-8") as file:
    try:
        file.write(' '.join([str(el) for el in random.sample(range(1, 100), 20)]))
        file.seek(0)
        sum_file = [sum([int(el) for el in line.split(' ')]) for line in file][0]
        print(sum_file)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
