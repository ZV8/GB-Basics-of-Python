class NotIntError(Exception):
    def __init__(self, txt):
        self.txt = txt


def return_digit(string):
    if string.isdigit():
        return int(string)
    else:
        try:
            return float(string)
        except ValueError:
            return False


my_list = []
while True:
    try:
        item = input('Введите число для добавления в список (или q для выхода): ')
        if item == 'q':
            break
        if return_digit(item):
            my_list.append(return_digit(item))
        else:
            raise NotIntError('Необходимо вводить только числа!')
    except NotIntError as err:
        print(err)

print(my_list)
