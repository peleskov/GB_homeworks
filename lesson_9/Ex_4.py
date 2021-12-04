class Car:
    def __init__(self, *args):
        self.speed, self.color, self.name, self.is_police = args

    def go(self):
        print(f'Car {self.name} ({self.color}){" is Police " if self.is_police else " "}start going')

    def stop(self):
        print(f'Car {self.name} ({self.color}){" is Police " if self.is_police else " "}stopped')

    def turn(self, direction):
        print(f'Car {self.name} ({self.color}){" is Police " if self.is_police else " "}turned {direction}')

    def show_speed(self):
        print(f'Car {self.name} ({self.color}){" is Police " if self.is_police else " "}going with speed {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Сar {self.name} ({self.color}) exceeded speed!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Сar {self.name} ({self.color}) exceeded speed!')


class PoliceCar(Car):
    pass


town_car = TownCar(90, 'red', 'Ford', False)
sport_car = SportCar(210, 'green', 'Porsche', False)
work_car = WorkCar(30, 'black', 'Skoda', False)
police_car = PoliceCar(50, 'white', 'Opel', True)
for car, direct in ((town_car, 'left'), (sport_car, 'right'), (work_car, 'right'), (police_car, 'back')):
    print(car.name)
    car.go()
    car.turn(direct)
    car.show_speed()
    car.stop()
