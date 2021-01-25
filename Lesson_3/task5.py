def sum_number():
    trigger = 0
    result = 0
    while trigger == 0:
        numbers = input('Ведите числа через пробел или нажмите q для выхода: ').split()
        current_result = 0
        for num in numbers:
            if 'q' in num:
                trigger = 1
                break
            current_result += int(num)
        result += current_result
        print(f'Сумма чисел: {result}, Enter для продолжения')
    return result

print(sum_number())