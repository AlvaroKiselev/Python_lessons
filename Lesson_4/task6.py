# a
from itertools import count, cycle

for i in count(int(input('Введите целое число: '))):
    if i <= 1000:
        print(i)
    else:
        print('Достаточно')
        break


# b
my_list = [1, 2, 3, 4, 5, 55, 8, 3, 9, 10, 15, 10]

iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()