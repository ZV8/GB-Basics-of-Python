my_list = [1, 3.14, 'Test', [1, 2], (3, 4), {'a': 100, 'b': 200}, True, None]
print(my_list)
for ind, el in enumerate(my_list):
    print(f'{ind} -> {el} имеет тип: {type(el)}')
