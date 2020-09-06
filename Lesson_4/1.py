from sys import argv


def my_zp(h, zp_h, zp_p):
    zp = (h * zp_h) + zp_p
    return zp


def argv_is_digit(a_):
    for arg in a_[1:]:
        if not is_digit(arg):
            return False
    return True


def is_digit(s_):
    if s_.isdigit():
        return True
    else:
        try:
            float(s_)
            return True
        except ValueError:
            return False


script, p_1, p_2, p_3 = argv
print(f'Переданные параметры:', p_1, p_2, p_3)

if argv_is_digit(argv):
    print('Итоговая з/п:', my_zp(float(p_1), float(p_2), float(p_3)))
else:
    print('Все параметры должны быть цифрами!')
