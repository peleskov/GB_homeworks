from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param
        self.__material = 0

    @abstractmethod
    def need_material(self):
        pass


class Coat(Clothes):
    @property
    def need_material(self):
        self.__material = round(self.param / 6.5 + 0.5, 2)
        return self.__material


class Suit(Clothes):
    @property
    def need_material(self):
        self.__material = round(self.param * 2 + 0.3, 2)
        return self.__material


coat = Coat(52)
suit = Suit(175)

print(coat.need_material)
print(suit.need_material)
print(coat.need_material + suit.need_material)
