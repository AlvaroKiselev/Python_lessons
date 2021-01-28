import sys

hours, salary, prize = map(float, sys.argv[1:])
print(f'Заработная плата: {hours * salary + prize}')

