def int_func(txt):
    list_txt = list(txt)
    for i, n in enumerate(list_txt):
        if (i == 0) & (ord(n) > 90):
            list_txt[i] = chr(ord(n) - 32)
        elif (i != 0) & (ord(n) < 91):
            list_txt[i] = chr(ord(n) + 32)
    return ''.join(list_txt)


def my_string(s):
    new_list = []
    list_s = s.split(' ')
    for i in list_s:
        new_list.append(int_func(i))
    return ' '.join(new_list)


new_string = my_string('dfff sdfdsf DSfsdgdDS dddDSdsdDSg sdg');
print(new_string)
