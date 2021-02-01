from math import factorial
from itertools import count


def fact():
    for i in count(1):
        yield factorial(i)


x = 1
for el in fact():
    print('Factorial {} - {}'.format(x, el))
    if x == 10:
        break
    x += 1