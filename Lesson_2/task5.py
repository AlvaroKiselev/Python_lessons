rate = [8, 6, 4, 4, 3, 3]
print('***Программа дополнения структуры рейтинга*** \nДля добавления нового элемента рейтинга напишите натуральное число и нажмите Enter. \nДля завершения ввода напишите exit и нажмите клавишу Enter')
list = []
while True:
    rate_element = input(f'Введите новое значение рейтинга и нажмите Enter: ')
    if rate_element == 'exit':
        break
    else:
        rate_element = int(rate_element)
        for i in range(len(rate)):
            if rate_element > rate[i]:
                rate.insert(i, rate_element)
                break
            elif rate_element == rate[i]:
                continue
            elif i == len(rate) - 1:
                rate.append(rate_element)

print(f'Актуализированный рейтинг:\n{rate}')