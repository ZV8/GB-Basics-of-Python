text = input('Введите строку из нескольких слов, разделённых пробелами: ')
list_text = text.split(' ')
for ind, el in enumerate(list_text):
    print(f'{ind + 1} -> {el[0:10:]}')
