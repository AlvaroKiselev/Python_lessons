array = []
total_value = 0
# создаем простые числа и добавляем кубы этих чисел в массив
current_number = 1
while current_number < 1000:
    if current_number % 2 == 0:
        current_number += 1
    array.append(current_number ** 3)
    current_number += 1

# задание А
for element in array:
    sum = 0
    current_number = element
    while current_number // 10 != 0:
        last_number = current_number % 10 # в переменную записываем крайнюю цифру в числе
        sum = sum + last_number
        current_number = current_number // 10
    sum = sum + current_number # добавляем самый старший разряд в сумму цифр

    # элемент массива, сумма цифр которого делится нацело на 7, добавляем в в переменную total_value
    if sum % 7 == 0:
        total_value = total_value + element
print('Cумма чисел из списка, сумма цифр которых делится нацело на 7: ', total_value)

# Задание
total_value = 0
new_array = []
for element in array:
    new_array.append(element + 17)

for element in new_array:
    sum = 0
    current_number = element
    while current_number // 10 != 0:
        last_number = current_number % 10 # в переменную записываем крайнюю цифру в числе
        sum = sum + last_number
        current_number = current_number // 10
    sum = sum + current_number # добавляем самый старший разряд в сумму цифр

    # элемент массива, сумма цифр которого делится нацело на 7, добавляем в в переменную total_value
    if sum % 7 == 0:
        total_value = total_value + element
print('Задание В. Cумма чисел из второго списка, сумма цифр которых делится нацело на 7: ', total_value)

# Задание С
total_value = 0

for i in range(len(array)):
    array[i] += 17

for element in array:
    sum = 0
    current_number = element
    while current_number // 10 != 0:
        last_number = current_number % 10 # в переменную записываем крайнюю цифру в числе
        sum = sum + last_number
        current_number = current_number // 10
    sum = sum + current_number # добавляем самый старший разряд в сумму цифр

    # элемент массива, сумма цифр которого делится нацело на 7, добавляем в в переменную total_value
    if sum % 7 == 0:
        total_value = total_value + element
print('Задание С. Cумма чисел из второго списка, сумма цифр которых делится нацело на 7: ', total_value)