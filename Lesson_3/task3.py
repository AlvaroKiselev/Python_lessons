def max2_f(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    try:
        min_number = min(my_list)
        return sum(my_list) - min_number
    except TypeError:
        print('Ошибка входных данных')

print(max2_f(12, 10, 6))