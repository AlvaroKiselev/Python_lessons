print('Давайте создадим список.\nДля сохранения элемента списка нажмите Enter. Для завершения ввода напишите exit и нажмите клавишу Enter')
i = 0
list = []
while True:
    list_element = input(f'Введите {i}-й элемент списка: ')
    i += 1
    if list_element == 'exit':
        break
    else:
        list.append(list_element)

print(f'Получился вот так список:\n{list}')
for i in range(0, (len(list) // 2) * 2, 2):
    buffer = list[i]
    list[i] = list[i+1]
    list[i+1] = buffer
print(f'А вот список с переставленными элементами:\n{list}')