print('Программа деления двух чисел')
first_number = float(input ('Введите первое число и нажмите Enter '))
second_number = float(input ('Введите второе число и нажмите Enter '))
def del_func(a, b):
    try:
        return print('Результат деления: ', a / b)
    except ZeroDivisionError:
        print("Деление на ноль невозможно. В следующий раз введите другое число")
    except TypeError:
        print("Ошибка ввода. Введите именно число")

del_func(first_number, second_number)

