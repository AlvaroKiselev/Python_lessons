with open('task5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())  # without list
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
print('Сумма чисел:', sum_nums)
