# ***Версия программы с использованием списков ***
month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
season_list = ['Зима', 'Весна', 'Лето', 'Осень']


while True:
    print('Версия программы с использованием списков')
    month_number = input('Введите номер месяца - число от 1 до 12, и нажмите Enter ')
    if month_number in number_list:
        if int(month_number) > 2 and int(month_number) < 6:
            season = 1
        elif int(month_number) > 5 and int(month_number) < 9:
            season = 2
        elif int(month_number) > 8 and int(month_number) < 12:
            season = 3
        else:
            season = 0
        print(f'{month_number}-й месяц это {month_list[int(month_number) - 1]}, {season_list[season]}')
        break
    else:
        print('Ошибка ввода. Пожалуйста введите целое число от 1 до 12 и нажмите Enter')
        continue

# ***Версия программы с использованием словаря ***
month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print('\nВерсия программы с использованием словаря')

while True:
    try:
        month_number = int(input('Введите номер месяца - число от 1 до 12, и нажмите Enter '))
        print(f'{month_number}-й месяц года это {month_dict[month_number]}')
        break
    except ValueError:
        print('Ошибка ввода. Необходимо ввести целое число от 1 до 12 и нажать Enter')
    except KeyError:
        print('Ошибка ввода. Необходимо ввести целое число от 1 до 12 и нажать Enter')


