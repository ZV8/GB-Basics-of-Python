from itertools import count, cycle


def my_count_cycle(start, stop, repeat):
    my_list = []
    my_repeat_list = []
    el = count(start)
    elem = next(el)
    while elem <= stop:
        my_list.append(elem)
        elem = next(el)
    cycle_list = cycle(my_list)
    i = 1
    while i <= repeat:
        my_repeat_list.append(next(cycle_list))
        i += 1
    return my_list, my_repeat_list


my_gen, my_rep = my_count_cycle(5, 10, 18)
print(my_gen)
print(my_rep)
