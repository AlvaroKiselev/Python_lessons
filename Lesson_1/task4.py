number = int(input("Программа поиска наибольшей цифры в числе. Введите число и нажмите Enter"))
biggest_number = 0
while number != 0:
    last_number = number % 10 # самый крайний разряд
    number = number // 10 # оставшиеся разряды
    if last_number > biggest_number:
        biggest_number = last_number

print('Наибольшая цифра в числе это', biggest_number)


