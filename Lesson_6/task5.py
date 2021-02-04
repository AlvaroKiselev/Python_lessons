class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('The pen is drawing')


class Pencil(Stationery):
    def draw(self):
        print('The pencil is drawing')


class Handle(Stationery):
    def draw(self):
        print('The handle is drawing')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()