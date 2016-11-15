from pico2d import*
import random

class Food_juel:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(40, 760), 160
        self. score = 0
        if Food_juel.image == None:
            self.image = load_image('Food_juel.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.score += 1
        self.x = random.randint(20, 780)


class Food_lave:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(40, 760), 160
        self.score = 0
        if Food_lave.image == None:
            self.image = load_image('Food_lave.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        self.score += 1
        self.x = random.randint(20, 780)

class HP:

    image = None

    def __init__(self):
        self.x, self.y = 777, 561
        self.state = 0
        if HP.image == None:
            self.image = load_image('HP.png')

    def draw(self):
        self.image.clip_draw(self.state * 46, 0, 46, 78, self.x, self.y)

    def update(self):
        self.state += 1
        if self.state > 3:
            self.state = 3

class MP:

    image = None

    def __init__(self):
        self.x, self.y = 23, 561
        self.state = 0
        if MP.image == None:
            self.image = load_image('MP.png')

    def draw(self):
        self.image.clip_draw(self.state * 46, 0, 46, 78, self.x, self.y)

    def update(self):
        self.state += 1
        if self.state > 3:
            self.state = 3