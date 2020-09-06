def fact(num):
    for i in range(1, num + 1):
        my_fact = 1
        for n in range(1, i + 1):
            my_fact = my_fact * n
        yield my_fact


for el in fact(5):
    print(el)
