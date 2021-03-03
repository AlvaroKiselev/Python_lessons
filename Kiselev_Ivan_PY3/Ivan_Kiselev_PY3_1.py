def num_translate(number):
    number_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number == number.lower():
        print(number_dict.get(number))
    elif number != number.lower():
        print(number_dict.get(number.lower()).capitalize())

number = input('Введите на английском буквенное название числа от 0 до 10: ')
num_translate(number)
