class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        __weight = 25
        __depth = 5
        return int(self._length * self._width * __weight * __depth / 1000)


road = Road(20, 5000)
print(road.calc())
