from pico2d import*

class gameover():
    def __init__(self):
        self.image = load_image('game_over.png')

    def draw(self):
        self.image.draw(400, 300)

class clear():

    def __init__(self):
        self.image = load_image('clear.png')

    def draw(self):
        self.image.draw(400,300)
