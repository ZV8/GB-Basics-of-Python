my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([elem for elem in my_list[1:] if my_list[my_list.index(elem)] > my_list[my_list.index(elem) - 1]])
