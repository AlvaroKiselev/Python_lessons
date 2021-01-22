def database_f(Name, Surname, year_of_birh, residence_city, email, telephone_number):
    data = {'Имя': Name, 'Фамилия': Surname, 'Год рождения': year_of_birh, 'Город проживания': residence_city,
            'Электронная почта': email, 'Номер телефона': telephone_number}
    print(data)

name = input('Имя: ')
surname = input('Фамилия: ')
date = input('Год рождения: ')
city = input('Город проживания: ')
email = input('Адрес электронной почты: ')
tel = input('Номер телефона: ')

database_f(Name=name, Surname=surname, year_of_birh=date, residence_city=city, email=email, telephone_number=tel)

