class Worker:
    def __init__(self, *args):
        self.name, self.surname, self.position, self._income = args


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position('Ivan', 'Ivanov', 'Manager', {'wage': 10000, 'bonus': 500})
print(pos.name)
print(pos.surname)
print(pos.position)
print(pos._income)
print(pos.get_full_name())
print(pos.get_total_income())
