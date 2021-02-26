# Дан список ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# Cформировать из обработанного списка строку
from pip._vendor.colorama import init

initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
digital_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
super_one = []

previous_found = False
for item in initial_list:
    if not previous_found:
        if item[0] in digital_list:
            initial_list.insert(initial_list.index(item), '"')
            initial_list.insert(initial_list.index(item) + 1, '"')

            if 9 >= int(item) >= -9:
                if item[0] in ['+', '-']:
                    initial_list[initial_list.index(item)] = item[0] + '0' + str(abs(int(item)))
                else:
                    initial_list[initial_list.index(item)] = '0' + item
            previous_found = True
    else:
        previous_found = False

print(initial_list)
for item in initial_list:
    if item == '"':
        index_element = initial_list.index(item)
        initial_list[index_element] = ''.join(initial_list[index_element:index_element + 3])
        del initial_list[index_element + 1]
        del initial_list[index_element + 1]

new_string = ' '.join(initial_list)
print(initial_list)
print(new_string)
