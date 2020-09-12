rename_num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("04.txt", "r", encoding="utf-8") as file:
    try:
        numerals = [rename_num[line.split(' ')[0]] + ' ' + line.split(' ')[1] + ' ' + line.split(' ')[2]
                    for line in file]
    except IOError:
        print("Произошла ошибка ввода-вывода!")

with open("04_new.txt", "w", encoding="utf-8") as new_file:
    try:
        new_file.write(''.join(numerals))
    except IOError:
        print("Произошла ошибка ввода-вывода!")
