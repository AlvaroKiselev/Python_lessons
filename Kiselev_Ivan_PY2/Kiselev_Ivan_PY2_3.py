name_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for name in name_list:
    name = name.split()
    name = name[-1].lower().capitalize()
    print(name)
