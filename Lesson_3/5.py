def input_num_sum(all_sum=0):
    nums = input('Введите строку чисел, разделенных пробелом: ').split(' ')
    for i, n in enumerate(nums):
        if n == 'q':
            nums = nums[:i]
            all_sum = my_sum(all_sum, nums)
            return all_sum
    all_sum = my_sum(all_sum, nums)
    input_num_sum(all_sum)


def my_sum(all_sum, nums):
    local_sum = sum(list(map(int, nums)))
    all_sum += local_sum
    print(f'{local_sum} ({all_sum})')
    return all_sum


input_num_sum()
