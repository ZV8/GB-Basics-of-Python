def my_func(a, b, c):
    if (a < b) & (a < c):
        return b + c
    if (b < a) & (b < c):
        return a + c
    return a + b


print(my_func(2, 1, 3))
