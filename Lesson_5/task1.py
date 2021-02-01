with open('text.txt', 'w') as file:
    while True:
        line = input('Введите строки для записи в файл. Для завершения нажмите Enter: ')
        if line == '':
            break
        file.write(line + '\n')