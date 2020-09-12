with open("03.txt", "r", encoding="utf-8") as file:
    try:
        less_20k = [line.split(' ')[0] for line in file if float(line.split(' ')[1]) < 20000]
        print(f"Сотрудники с окладом менее 20 тыс:\n{', '.join(less_20k)}")
    except IOError:
        print("Произошла ошибка ввода-вывода!")

with open("03.txt", "r", encoding="utf-8") as file:
    try:
        salary = [float(line.split(' ')[1]) for line in file]
        print(f"Средняя величина дохода сотрудников:\n{round(sum(salary) / len(salary), 2)}")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
