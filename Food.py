from pico2d import*
import random

class Food_juel:
    image = None

    def __init__(self):
        self.x, self.y = 150, 160
        self. score = 0
        if Food_juel.image == None:
            self.image = load_image('Food_juel.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.score += 1
        self.x = random.randint(20, 780)


class Food_lave:
    image = None

    def __init__(self):
        self.x, self.y = 650, 160
        self.score = 0
        if Food_lave.image == None:
            self.image = load_image('Food_lave.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.score += 1
        self.x = random.randint(20, 780)
