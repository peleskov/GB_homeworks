class Cell:
    def __init__(self, qty):
        self.qty = int(qty)

    def __str__(self):
        return f'{self.qty}'

    def __add__(self, other):
        return Cell(self.qty + other.qty)

    def __sub__(self, other):
        res = self.qty - other.qty
        if res > 0:
            return Cell(res)
        else:
            return 'Операция не возможна'

    def __mul__(self, other):
        return Cell(self.qty * other.qty)

    def __floordiv__(self, other):
        if self.qty > other.qty:
            return Cell(self.qty // other.qty)
        else:
            return 'Операция не возможна'

    def __truediv__(self, other):
        # не нашел как объединить два метода с одинаковым функционалом __floordiv__ и __truediv__
        if self.qty > other.qty:
            return Cell(self.qty // other.qty)
        else:
            return 'Операция не возможна'

    def make_order(self, div):
        return (('*' * div) + '\n') * (self.qty // div) + '*' * (self.qty % div)


cell1 = Cell(5)
cell2 = Cell(84)
cell3 = cell1 + cell2
print(cell3)
cell3 = cell2 - cell1
print(cell3)
cell3 = cell1 - cell2
print(cell3)
cell3 = cell1 * cell2
print(cell3)
cell3 = cell1 // cell2
print(cell3)
cell3 = cell2 // cell1
print(cell3)
cell3 = cell2 / cell1
print(cell3)
print(cell1)
print(cell3.make_order(7))
