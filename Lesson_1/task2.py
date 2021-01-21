time = int(input('Введите время в секундах для перевода в часы/минуты/секунды:'))
hours = time // 3600;
# minutes = (time - hours * 3600) // 60
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60
print(f'Время {hours}:{minutes}:{seconds}')