with open('text.txt') as file:
    lines = file.readlines()
print('Количество строк: ', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} строка содержит {} слов'.format(num_line, len(line.split())))