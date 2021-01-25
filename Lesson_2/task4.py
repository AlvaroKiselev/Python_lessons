string = input('Введите строку из нескольких слов, разделенных пробелами и нажмите Enter ')
string = string.split()
for i in range(len(string)):
    print(f'{i + 1}. {string[i][0:10]}')