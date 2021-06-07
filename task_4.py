

class Car():

    def __init__(self, name, speed, color, turn_around, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        self.turn_around = turn_around


    def go(self):
        print('the cars gone')


    def stop(self):
        print('the car stopped')


    def turn(self):
        print(f'the car turned {self.turn_around}')


    def show_speed(self):
        print(f'current vehicle speed: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if 60 < self.speed:
            print('Speeding! Slow down to 60')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if 40 < self.speed:
            print('Speeding! Slow down to 40')


if __name__ == '__main__':
    town_car = TownCar('ambulance', 90, 'blue', 'wrong turn', False)
    town_car.show_speed()
    town_car.turn()