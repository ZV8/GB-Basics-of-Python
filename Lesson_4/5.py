from functools import reduce

print(reduce(lambda prev_el, el: prev_el * el, [elem for elem in range(100, 1001) if elem % 2 == 0]))
