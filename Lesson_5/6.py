with open("06.txt", "r", encoding="utf-8") as file:
    try:
        print({line.split(' ')[0]: sum(
            list(map(lambda y: int(y.split('(')[0]),
                     filter(lambda x: x and x != '—' and x != '—\n', line.split(' ')[1:])))) for line in file})
    except IOError:
        print("Произошла ошибка ввода-вывода!")
