from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = [('красный', 7), ('желтый', 2), ('зеленый', 3)]

    def running(self):
        for col, sec in cycle(self.__color):
            print(col)
            sleep(sec)


item = TrafficLight()
print(item.running())
