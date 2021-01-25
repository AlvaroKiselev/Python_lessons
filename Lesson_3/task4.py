def my_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Ошибка ввода данных'
    return result

a = int(input('Введите действительное положительное число: '))
b = int(input('Введите степень числа (целое отрицательное число): '))
print(my_func(a, b))


# Вариант без **
def my_func2(x, y):
    try:
        result = 1 / x
        for i in range(abs(y) - 1):
            result = result / x
        return result
    except ValueError:
        return 'Ошибка ввода данных'

print(my_func2(a, b))