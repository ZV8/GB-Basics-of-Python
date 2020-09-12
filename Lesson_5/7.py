import json

with open("07.txt", "r", encoding="utf-8") as file:
    try:
        firms = {}
        for line in file:
            data_line = line.split(' ')
            profit = int(data_line[2]) - int(data_line[3])
            firms[data_line[0]] = profit
    except IOError:
        print("Произошла ошибка ввода-вывода!")

positive_profit = list(filter(lambda x: x >= 0, firms.values()))
average_profit = {'average_profit': sum(positive_profit) / len(positive_profit)}
obj = [firms, average_profit]

with open("07.json", "w", encoding="utf-8") as w_file:
    try:
        json.dump(obj, w_file)
        print("Данные успешно записаны в файл")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
