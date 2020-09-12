with open("02.txt", "r", encoding="utf-8") as file:
    try:
        print(f'Количество строк в файле: {sum([1 for line in file])}')
    except IOError:
        print("Произошла ошибка ввода-вывода!")


with open("02.txt", "r", encoding="utf-8") as file:
    try:
        print('Количество слов в каждой строке: ')
        for line in file:
            words = len(line.split(' '))
            print(words)
    except IOError:
        print("Произошла ошибка ввода-вывода!")
