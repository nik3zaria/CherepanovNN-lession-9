

class Road():
    WEB_THICKNESS_CM = 5      #we measure it in centimeters
    WEIGHT_OF_ASPHALT = 25    #by 1 centimeter
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculating_the_mass(self):
        return ((self._width * self._length * self.WEIGHT_OF_ASPHALT * self.WEB_THICKNESS_CM) / 1000)


if __name__ == '__main__':
    width_user = input('Введите ширину асфальта: ')
    length_user = input('Введите длину асфальта: ')
    road = Road(int(length_user), int(width_user))
    print(f'{road.calculating_the_mass()} тонн')