goods_list = []
analitics = {'Название': [], 'Цена': [], 'Количество': [], 'Ед': []}
number = 0
attributes = {'Название': '', 'Цена': '', 'Количество': '', 'Ед': ''}
while True:
    if input('Для продолжения нажмите любую клавишу и нажмите Enter. \nДля выхода введите exit и нажмите Enter ').lower() == 'exit':
        break
    else:
        number += 1
    for type in attributes.keys():
        user_data = input(f'{type}: ')
        attributes[type] = user_data if (type == 'Название' or 'Ед') else int(user_data)
        analitics[type].append(attributes[type])
    goods_list.append((number, attributes.copy()))
    #print(goods_list)
    print('Аналитика по товарам: \n')
    for key, value in analitics.items():
        print(key, value)
