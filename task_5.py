

class Stationary():

    def __init__(self, title):
        self.title = title


    def draw(self):
        print('starting the rendering')


class Pen(Stationary):
    def draw(self):
        print('drawing a pen')


class Pencil(Stationary):
    def draw(self):
        print('drawing a pencil')


class Handle(Stationary):
    def draw(self):
        print('drawing a handle')


