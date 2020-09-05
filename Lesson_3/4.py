def my_func(x, y):
    return abs(x) ** -int(abs(y))


def my_func2(x, y):
    n = abs(x)
    for i in range(1, int(abs(y))):
        n = n * abs(x)
    return 1 / n


print(my_func(2, 3))
print(my_func2(2, 3))
