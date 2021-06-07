from time import sleep


class TrafficLight():
    def __init__(self):
        self.__color = None

    def running(self):
        self.__color = 'Зеленый'
        yield self.__color
        sleep(7)
        self.__color = 'Желтый'
        yield self.__color
        sleep(7)
        self.__color = 'Крсный'
        yield self.__color
        sleep(7)


if __name__ == '__main__':
    traffik_light = TrafficLight()
    lights = []

    for light in traffik_light.running():
        lights.append(light)

    if (lights == ['Зеленый', 'Желтый', 'Красный']):
        print('Светофор работает исправно.')
    else:
        assert (lights == ['Зеленый', 'Желтый', 'Красный']), 'Что то сломалось, светофору требуется ремонт.'