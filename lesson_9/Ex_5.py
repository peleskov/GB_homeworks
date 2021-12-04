class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title.title()} рисует')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title.title()} рисует')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title.title()} рисует')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()
