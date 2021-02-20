number = ''
last_part = ['ов', '', 'а', 'а', 'а', 'ов', 'ов', 'ов', 'ов', 'ов']
while number != 'q':
    number = input('Введите число процента для склонения или нажмите q для завершения работы: ')
    if number == 'q':
        break
    elif number == '11':
        print(f'{number} процент{last_part[0]}')
    else:
        print(f'{number} процент{last_part[int(number) % 10]}')

