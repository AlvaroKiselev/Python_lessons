duration = float(input("Введите временной промежуток в секундах и нажмите Enter: "))

hours = (duration // 3600) % 24;
minutes = (duration % 3600) // 60
seconds = (duration % 3600) % 60
days = duration // 86400
if duration < 60:
    print(f'duration = {duration} сек')
elif duration >= 60 and duration < 3600:
    print(f'Duration = {minutes} мин {seconds} сек')
elif duration >= 3600 and duration < 86400:
    print(f'Duration = {hours} часов {minutes} мин {seconds} сек')
else:
    print(f'Duration = {days} суток {hours} часов {minutes} мин {seconds} сек')